
from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import RedirectView

import apps.control.views as ControlViews
import apps.auth.views as AuthViews

urlpatterns = patterns('',
    url(r'^favicon\.ico$', RedirectView.as_view(url=settings.STATIC_URL + 'img/favicon.ico')),
    url(r'^$', ControlViews.DashboardView.as_view(), name='dashboard'),
    url(r'^time$', ControlViews.TimeView.as_view(), name='time'),
    url(r'^config$', ControlViews.ConfigView.as_view(), name='config'),
    url(r'^switch/(?P<device_id>\w+)/(?P<switch>\w+)$', ControlViews.SwitchView.as_view(), name='switch'),
    url(r'^operate/(?P<device_id>\w+)/(?P<operation>\w+)$', ControlViews.OperateView.as_view(), name='operate'),
    url(r'^operation_log/(?P<device_id>\w+)/(?P<operation_log_id>\d+)$', ControlViews.OperationLogView.as_view(), name='operation_log'),
    url(r'^event/(?P<event_id>\d+)/(?P<device_id>\w+)$', ControlViews.EventView.as_view(), name='event'),

    url(r'^login$', AuthViews.LoginView.as_view(), name='login'),
    url(r'^logout$', AuthViews.LogoutView.as_view(), name='logout'),
    url(r'^register$', AuthViews.RegisterView.as_view(), name='register'),
)
