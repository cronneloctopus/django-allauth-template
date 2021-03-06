from django.conf.urls import patterns, include, url
from django.conf import settings
from django.views.generic import TemplateView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^$', 'django_allauth_template.views.home', name='home'),

    url(r'^accounts/', include('allauth.urls')),

    url(r'^', TemplateView.as_view(template_name="home.html")),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
)

##  local static and media settings
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        (r'^static/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        (r'^media/(?P<path>.*)$',
        'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
