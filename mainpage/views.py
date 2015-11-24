from django.shortcuts import render
from mainpage.search import get_query
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from uploader.models import Document, Report
from uploader.forms import DocumentForm, reportEditForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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
    query_string = ''
    found_entries = None
    form = DocumentForm()
    documents = Document.objects.all()
    reports = Report.objects.all()
    
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
        	
        return render_to_response(
            'publicReports.html',
            {'reports': found_reports, 'documents': documents, 'form':form, 'query':query_string},
            context_instance=RequestContext(request)
            )
    else:
        if ( request.GET.get('sortselect') == "namerb" ):
        	reports = reports.order_by("name")
        if ( request.GET.get('sortselect') == "userrb" ):
        	reports = reports.order_by("user")
        if ( request.GET.get('sortselect') == "daterb" ):
        	reports = reports.order_by("timestamp")
        
        return render_to_response(
            'publicReports.html',
            {'reports': reports, 'documents': documents, 'form':form, 'query':False},
            context_instance=RequestContext(request)
            )

@login_required(login_url='login')
def myReports(request):
    form = DocumentForm()
    documents = Document.objects.all()
    reports = Report.objects.all()

    return render_to_response(
        'myReports.html',
        {'reports': reports, 'documents': documents, 'form': form},
        context_instance=RequestContext(request)
        )

@login_required(login_url='login')
def logout_view(request):
    logout(request);
    return render(request, 'index.html')
