from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf import settings
admin.site.site_header = settings.ADMIN_SITE_HEADER


urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),
    url(r'^model/', include('QuotesModel.urls')),
)

urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))

urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))