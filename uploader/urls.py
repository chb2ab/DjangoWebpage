# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('uploader.views',
    url(r'^list/$', 'list', name='list'),
    url(r'^editreport/$', 'editreport', name='editreport'),
    url(r'^deletereport/$', 'deletereport', name='deletereport'),
    url(r'^deletedocument/$', 'deletedocument', name='deletedocument'),
    url(r'^uploaddocument/$', 'uploaddocument', name='uploaddocument'),
    url(r'^addreport/$', 'addreport', name='addreport'),
    url(r'^(?P<groupName>[a-z0-9]+)/addgroupmember/(?P<userName>[a-z0-9]+)/$', views.addgroupmember, name='addgroupmember'),
    url(r'^(?P<groupName>[a-z0-9]+)/addgroupreport/$', views.addgroupreport, name='addgroupreport'),
    url(r'^addfolder/$', 'addfolder', name='addfolder'),
    url(r'^editfolder/$', 'editfolder', name='editfolder'),
    url(r'^addgroup/$', 'addgroup', name='addgroup'),
    url(r'^(?P<groupName>[a-z0-9]+)/addgroupmember/$', views.groupuserlist, name='groupuserlist'),
    url(r'^deletefolder/$', 'deletefolder', name='deletefolder'),
    url(r'^userlist/$', views.userlist , name='userlist'),
    url(r'^(?P<group2_name>[a-z0-9]+)/$', views.grouptest, name='grouptest'),
)
