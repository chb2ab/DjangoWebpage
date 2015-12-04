from django.conf.urls import url

from . import views 

urlpatterns = [
    url(r'^$', views.mainpage, name='mainpage'),
    url(r'^myReports/$', views.myReports, name='myReports'),
    url(r'^publicReports/$', views.publicReports, name='publicReports'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^delete/$', views.delete_view, name='delete'),
]
