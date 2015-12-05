from django.shortcuts import render
from mainpage.search import get_query
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from uploader.models import Document, Report, Folder, Group2
from uploader.forms import DocumentForm, reportEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
import pdb;
# Create your views here.

@login_required(login_url='login')
def mainpage(request):
	form = DocumentForm()

	documents = Document.objects.all()
	reports = Report.objects.all()

	return render_to_response(
		'mainpage.html',
		{'reports': reports, 'documents': documents, 'form':form},
		context_instance=RequestContext(request)
		)
   
@login_required(login_url='login')
def publicReports(request):
	if ('upvote' in request.POST):
		rep = Report.objects.get( pk=int(request.POST['upvote']) )
		if rep.votes.exists(request.user):
			print("already upvoted")
		else:
			rep.votes.up(request.user)
		
	if ('downvote' in request.POST):
		rep = Report.objects.get( pk=int(request.POST['downvote']) )
		rep.votes.down(request.user)

	query_string = ''
	found_entries = None
	form = DocumentForm()
	documents = Document.objects.all()
	reports = Report.objects.all()
	voted = None;
	if len(reports) > 0:
		r1 = reports[0];
		voted = r1.votes.all( request.user )

	if ('q' in request.GET) and request.GET['q'].strip():
		query_string = request.GET['q']
		
		found_reports = reports
		fields = []
		if ( request.GET.get('namecb') == "on" ):
			fields.append('name')
			
		if ( request.GET.get('sdcb') == "on" ):
			fields.append('sd')
			
		if ( request.GET.get('ldcb') == "on" ):
			fields.append('ld')
			
		if ( request.GET.get('usercb') == "on" ):
			fields.append('user')
		
		if ( len(fields) > 0 ):
			report_query = get_query(query_string, fields)
			found_reports = found_reports.filter(report_query)
		
		if ( request.GET.get('sortselect') == "namerb" ):
			found_reports = found_reports.order_by("name")
		if ( request.GET.get('sortselect') == "userrb" ):
			found_reports = found_reports.order_by("user")
		if ( request.GET.get('sortselect') == "daterb" ):
			found_reports = found_reports.order_by("timestamp")
		if ( request.GET.get('sortselect') == "votesb" ):
			found_reports = sorted( found_reports, key=lambda report: int(report.votes.count()), reverse=True )
		
		return render_to_response(
			'publicReports.html',
			{'reports': found_reports, 'documents': documents, 'form':form, 'query':query_string, 'voted':voted},
			context_instance=RequestContext(request)
			)
	else:
		if ( request.GET.get('sortselect') == "namerb" ):
			reports = reports.order_by("name")
		if ( request.GET.get('sortselect') == "userrb" ):
			reports = reports.order_by("user")
		if ( request.GET.get('sortselect') == "daterb" ):
			reports = reports.order_by("timestamp")
		if ( request.GET.get('sortselect') == "votesb" ):
			reports = sorted( reports, key=lambda report: int(report.votes.count()), reverse=True )
	
		return render_to_response(
			'publicReports.html',
			{'reports': reports, 'documents': documents, 'form':form, 'query':False, 'voted':voted},
			context_instance=RequestContext(request)
			)
	
@login_required(login_url='login')
def myReports(request):
	form = DocumentForm()
	documents = Document.objects.all()
	reports = Report.objects.all()
	folders = Folder.objects.all()
	

	return render_to_response(
		'myReports.html',
		{'reports': reports, 'documents': documents, 'form': form, 'folders': folders},
		context_instance=RequestContext(request)
		)

@login_required(login_url='login')
def profile(request):
    reports = Report.objects.all()
    users = User.objects.all()
    return render_to_response(
        'profile.html',
        {'users':users, 'reports':reports},
        context_instance=RequestContext(request)
        )

@login_required(login_url='login')
def map(request):
    reports = Report.objects.all()
    users = User.objects.all()
    return render_to_response(
        'map.html',
        {'reports': reports},
        context_instance=RequestContext(request)
    )


def myGroups(request):
    groups = Group2.objects.all()

    return render_to_response(
        'myGroups.html',
        {'groups': groups},
        context_instance=RequestContext(request)
        )

@login_required(login_url='login')
def logout_view(request):
	logout(request);
	return render(request, 'index.html')

@login_required(login_url='login')
def delete_view(request):
	reports = Report.objects.all()
	folders = Folder.objects.all()
	
	query = get_query(request.user.username, ['user'])
	
	reports_to_delete = reports.filter(query)
	folders_to_delete = folders.filter(query)
	
	for report in reports_to_delete:
		report.delete()
	for folder in folders_to_delete:
		folder.delete()
		
	request.user.delete()
	
	logout(request);
	return render(request, 'index.html')
