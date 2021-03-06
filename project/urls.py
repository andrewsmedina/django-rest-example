from django.conf.urls.defaults import patterns, include, url

from services.api import ServiceResource

from django.contrib import admin
admin.autodiscover()

service_resource = ServiceResource()

urlpatterns = patterns('',
    (r'^api/', include(service_resource.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
