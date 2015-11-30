# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import pdb;

from uploader.models import Document, Report, Folder
from uploader.forms import DocumentForm, reportEditForm, folderEditForm

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
	form.fields['folder'].queryset = Folder.objects.filter(user=request.user)
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

@login_required(login_url='login')
def editfolder(request):
	id = request.POST.get("idoffolder", None);
	instance = get_object_or_404(Folder, id=id)
	form = folderEditForm(request.POST or None, instance=instance)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/mainpage/myReports')
		
	form = folderEditForm(instance=instance)
	return render_to_response(
		'editfolder.html',
		{'form': form, 'idoffolder': id},
		context_instance=RequestContext(request)
	)
