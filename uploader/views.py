# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import pdb;

from uploader.models import Document, Report, Folder, Group2
from uploader.forms import DocumentForm, reportEditForm, folderEditForm, groupEditForm


def userlist(request):
	users = User.objects.all()
	return render_to_response(
		'userlist.html',
		{'users': users},
		context_instance=RequestContext(request)
		)


@login_required(login_url='login')
def list(request):
	form = DocumentForm() # A empty, unbound form

	# Load documents for the list page
	documents = Document.objects.all()
	reports = Report.objects.all()

	# Render list page with the documents and the form
	return render_to_response(
		'list.html',
		{'reports': reports, 'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

def groupList(request):
	groups = Group2.objects.all()
	return render_to_response(
		'myGroups.html',
		{'groups': groups},
		context_instance=RequestContext(request)
		)

@login_required(login_url='login')
def publicList(request):
	form = DocumentForm()

	documents = Document.objects.all()
	reports = Report.objects.all()
	return render_to_response(
		'mainpage.html',
		{'reports': reports, 'documents': documents, 'form': form},
		context_instance=RequestContext(request)
	)

def groupuserlist(request, groupName):
	groups = Group2.objects.all()
	users = User.objects.all()

	return render_to_response(
		'addgroupmember.html',
		{'groups':groups, 'users':users, 'group':groupName},
		context_instance=RequestContext(request)
		)

def addgroupmember(request, userName, groupName):
	groups = Group2.objects.all()
	users = User.objects.all()
	#NOTE : For some reason, group name and user name are switched
	# I will figure out this problem later::::
	for group in groups:
		if group.name == userName:
			for user in users:
				if user.username == groupName:
					group.permissions.add(user)
	#return HttpResponseRedirect('uploader/' + groupName)				
	return render_to_response(
		'addnewgroupmember.html',
		{'useradded': groupName, 'group':userName},
		context_instance=RequestContext(request)
		)

def addgroupreport(request, groupName):
	body = Report(user=request.user)
	groups = Group2.objects.all()
	form = reportEditForm(request.POST, instance=body)
	if form.is_valid():
		form.save()
		for group in groups:
			if group.name == groupName:
				group.reports.add(body)
		return HttpResponseRedirect('/uploader/' + groupName)
	else:
		form = reportEditForm(instance=body)
		form.fields['folder'].queryset = Folder.objects.filter(user=request.user)
		for group in groups:
			if group.name == groupName:

				return render_to_response(
				'addgroupreport.html',
				{'form': form, 'group': group},
				context_instance=RequestContext(request)
				)



@login_required(login_url='login')
def addreport(request):

	#id = request.POST.get("idofreport", None);
	#instance = get_object_or_404(Report, id=id)
	#documents = instance.document_set.all()

	body = Report(user=request.user)
	form = reportEditForm(request.POST, instance=body)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/mainpage/myReports')
	
	else:
		form = reportEditForm(instance=body)
		form.fields['folder'].queryset = Folder.objects.filter(user=request.user)
		return render_to_response(
		'addreport.html',
		{'form': form},
		context_instance=RequestContext(request)
		)

@login_required(login_url='login')
def deletereport(request):
	id = request.POST.get("idofreport", None);
	Report.objects.get(pk=id).delete()
	
	return HttpResponseRedirect('/mainpage/myReports')


@login_required(login_url='login')
def deletefolder(request):
	id = request.POST.get("idoffolder", None);
	Folder.objects.get(pk=id).delete()
	
	return HttpResponseRedirect('/mainpage/myReports')

@login_required(login_url='login')
def editreport(request):
	id = request.POST.get("idofreport", None);
	instance = get_object_or_404(Report, id=id)
	documents = instance.document_set.all()
	form = reportEditForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/mainpage/myReports')
		
	form = reportEditForm(instance=instance)
	uploadform = DocumentForm()
	return render_to_response(
		'editreport.html',
		{'form': form, 'idofreport': id, 'documents': documents, 'uploadform': uploadform},
		context_instance=RequestContext(request)
	)

@login_required(login_url='login')
def deletedocument(request):
	docid = request.POST.get("idofdoc", None)
	Document.objects.get(pk=docid).delete()
	return editreport(request)

def grouptest(request, group2_name):
	groups = Group2.objects.all()
	a = False
	for group in groups:
		if (group.name == group2_name):
			a = True
			if group.creator == request.user.username:
				return render(request, 'uploader/grouptest.html', {'group':group})
				#return HttpResponse("You're looking at group %s. " % group2_name)
			for user in group.permissions.all():
				if user.username == request.user.username:
					return HttpResponse("You're looking at group %s. " % group2_name)

	if (a):
		return HttpResponse("You do not have the access to view this group")
	return HttpResponse("Unfortunately, this group does not exist yet")

@login_required(login_url='login')
def uploaddocument(request):
	# Handle file upload
	form = DocumentForm(request.POST, request.FILES)
	
	repid = request.POST.get("idofreport", None);
	instance = get_object_or_404(Report, id=repid)
	
	if form.is_valid():
		newdoc = Document(docfile = request.FILES['docfile'], report=instance, encrypted = request.POST.get('encrypt', False))
		newdoc.save()
	
	return editreport(request)
	
@login_required(login_url='login')
def addfolder(request):
	body = Folder(user=request.user)
	form = folderEditForm(request.POST, instance=body)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/mainpage/myReports')
	else:
		form = folderEditForm()
		return render_to_response(
		'addfolder.html',
		{'form': form},
		context_instance=RequestContext(request)
		)

def addgroup(request):
	body = Group2(creator=request.user)
	form = groupEditForm(request.POST, instance=body)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/mainpage/myGroups')
	else:
		form = groupEditForm()
		return render_to_response(
		'addgroup.html',
		{'form':form},
		context_instance=RequestContext(request)
		)
