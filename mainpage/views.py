from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from uploader.models import Document, Report
from uploader.forms import DocumentForm, reportEditForm
import pdb;
# Create your views here.

def mainpage(request):
    form = DocumentForm()

    documents = Document.objects.all()
    reports = Report.objects.all()

    return render_to_response(
        'mainpage.html',
        {'reports': reports, 'documents': documents, 'form':form},
        context_instance=RequestContext(request)
        )
   
def publicReports(request):
    form = DocumentForm()
    documents = Document.objects.all()
    reports = Report.objects.all()

    return render_to_response(
        'publicReports.html',
        {'reports': reports, 'documents': documents, 'form':form},
        context_instance=RequestContext(request)
        )

def myReports(request):
    form = DocumentForm()
    documents = Document.objects.all()
    reports = Report.objects.all()

    return render_to_response(
        'myReports.html',
        {'reports': reports, 'documents': documents, 'form': form},
        context_instance=RequestContext(request)
        )
