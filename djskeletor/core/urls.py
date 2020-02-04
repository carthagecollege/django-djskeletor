# -*- coding: utf-8 -*-

"""URLs for all views."""

from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include
from django.urls import path
from django.urls import reverse_lazy
from django.views.generic import RedirectView
from django.views.generic import TemplateView

from djauth.views import loggedout


admin.autodiscover()

handler404 = 'djtools.views.errors.four_oh_four_error'
handler500 = 'djtools.views.errors.server_error'


urlpatterns = [
    # auth
    path(
        'accounts/login/',
        auth_views.LoginView.as_view(),
        {'template_name': 'accounts/login.html'},
        name='auth_login',
    ),
    path(
        'accounts/logout/',
        auth_views.LoginView.as_view(),
        {'next_page': reverse_lazy('auth_loggedout')},
        name='auth_logout',
    ),
    path(
        'accounts/loggedout/',
        loggedout,
        {'template_name': 'accounts/logged_out.html'},
        name='auth_loggedout',
    ),
    path(
        'accounts/',
        RedirectView.as_view(url=reverse_lazy('auth_login')),
    ),
    path(
        'denied/',
        TemplateView.as_view(template_name='denied.html'),
        name='access_denied',
    ),
    # django admin and loginas
    path('rocinante/', include('loginas.urls')),
    path('rocinante/', admin.site.urls),
    # admin honeypot
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # my app
    path('myapp/', include('djskeletor.myapp.urls')),
    # dashboard
    path('dashboard/', include('djskeletor.dashboard.urls')),
    # direct to template
    path('success/', TemplateView.as_view(template_name='myapp/success.html')),
    # redirect
    path('', RedirectView.as_view(url=reverse_lazy('dashboard_home'))),
]
