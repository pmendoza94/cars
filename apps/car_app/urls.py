from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add$', views.add),
    url(r'^submit_car$', views.submit_car),
    url(r'^all$', views.all),
    url(r'^own/(?P<car_id>\d+)/(?P<user_id>\d+)$', views.own),
    url(r'^unown/(?P<car_id>\d+)/(?P<user_id>\d+)$', views.unown),
    url(r'^show/(?P<user_id>\d+)$', views.show),
]
