from django.shortcuts import render
from mainpage.search import get_query
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from uploader.models import Document, Report, Folder, Group2
from uploader.forms import DocumentForm, reportEditForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import logout
from uploader.forms import DocumentForm, reportEditForm, folderEditForm, groupEditForm
from siteadmin.models import admin
import pdb;

# Create your views here.

def mainpage(request):

	reports = Report.objects.all()

	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')
	return render_to_response(
		'siteadminmain.html',
		{'reports': reports},
		context_instance=RequestContext(request)
		)

def userlist(request):
	users = User.objects.all()
	reports = Report.objects.all()
	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')
	return render_to_response(
		'users.html',
		{'users': users, 'reports':reports},
		context_instance=RequestContext(request)
		)

def userinfo(request, user_name):
	users = User.objects.all()
	reports = Report.objects.all()
	groups = Group2.objects.all()
	documents = Document.objects.all()
	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')

	for user in users:
		if user.username == user_name:
			return render(request, 'siteadmin/userinfo.html', {'reports':reports, 'groups':groups, 'documents':documents, 'user_name':user_name, 'user':user})

	return HttpResponseRedirect('/siteadmin/')


def suspendaccount(request, user_name):
	users = User.objects.all()
	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')
	for user in users:
		if user.username == user_name:
			user.is_active = True
			user.save()
	return HttpResponseRedirect('/siteadmin/' + user_name)

def unsuspendaccount(request, user_name):
	users = User.objects.all()
	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')
	for user in users:
		if user.username == user_name:
			user.is_active = False
			user.save()
	return HttpResponseRedirect('/siteadmin/' + user_name)

def admins(request):
	users = User.objects.all()
	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')
	admins = admin.objects.all()
	return render(request, 
		'siteadmin/admins.html',
		{'users':users, 'admins': admins}
		)

def groups(request):
	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')
	groups = Group2.objects.all()
	return render_to_response(
        'groups.html',
        {'groups': groups},
        context_instance=RequestContext(request)
        )

def newadmin(request, user_name):
	if not request.user.is_staff:
		return HttpResponseRedirect('/mainpage/')
	users = User.objects.all()
	user_name_added = user_name
	groups = Group2.objects.all()
	for user in users:
		if user.username == user_name:
			user.is_staff = True
			user.save()
	return render(request, 'siteadmin/admins.html',
		{'groups':groups, 'users':users}
		)

def groupvis(request):
	groups = Group2.objects.all()
	users = User.objects.all()

	return render_to_response(
		'visualization.html',
		{'groups':groups, 'users':users},
		context_instance=RequestContext(request)
		)


