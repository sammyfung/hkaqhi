from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
    url(r'^hourly/$', views.hourly_data),
    url(r'^station/$', views.station_data),
)
