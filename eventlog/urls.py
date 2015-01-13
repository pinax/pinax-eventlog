from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns('',
                       url(r'^api/add/', views.LogEventCreate.as_view(), name='eventlog_api_add'),)
