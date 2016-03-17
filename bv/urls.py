from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^workers/', include('workers.urls')),
    url(r'^stores/', include('stores.urls')),
    url(r'^profiles/', include('profiles.urls')),
    url(r'^reports/', include('reports.urls')),
    url(r'^customers/', include('customers.urls')),
    #url(r'^api/', include('api.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework'))
]
