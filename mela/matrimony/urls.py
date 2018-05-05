from django.conf.urls import patterns, url

from matrimony import views

urlpatterns = [ 
url(r'^$', views.ApplicationList.as_view(), name='application_list'),
url(r'^new$', views.ApplicationCreate.as_view(), name='application_new'),
url(r'^detail/(?P<pk>\d+)$', views.ApplicationDetail.as_view(), name='application_detail'),
url(r'^edit/(?P<pk>\d+)$', views.ApplicationUpdate.as_view(), name='application_edit'),
url(r'^delete/(?P<pk>\d+)$', views.ApplicationDelete.as_view(), name='application_delete'),
]
