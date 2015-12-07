from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^profile/killswitch/$', views.killswitch, name='killswitch'),
    url(r'^myReports/$', views.myReports, name='myReports'),
    url(r'^myGroups/$', views.myGroups, name='myGroups'),
    url(r'^publicReports/$', views.publicReports, name='publicReports'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^delete/$', views.delete_view, name='delete'),
    url(r'^profile/map/$', views.map, name='map'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/statistics/$', views.statistics, name='statistics'),
]
