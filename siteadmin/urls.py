from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^admins/$', views.admins, name='admins'),
    url(r'^admins/(?P<user_name>[a-z0-9]+)$', views.newadmin, name='newadmin'),
    url(r'^users/$', views.userlist, name='userlist'),
    url(r'^groups/$', views.groups, name='groups'),
    url(r'^groups/visualization/$', views.groupvis, name='groupvis'),

    url(r'^(?P<user_name>[a-z0-9]+)/$', views.userinfo, name='userinfo'),
    url(r'^(?P<user_name>[a-z0-9]+)/suspendaccount$', views.suspendaccount, name='suspendaccount'),
    url(r'^(?P<user_name>[a-z0-9]+)/unsuspendaccount$', views.unsuspendaccount, name='unsuspendaccount'),


]
