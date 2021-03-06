# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url

urlpatterns = patterns('uploader.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^editreport/$', 'editreport', name='editreport'),
    url(r'^deletereport/$', 'deletereport', name='deletereport'),
    url(r'^deletedocument/$', 'deletedocument', name='deletedocument'),
    url(r'^uploaddocument/$', 'uploaddocument', name='uploaddocument')
)
