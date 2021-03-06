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
    url(r'^company/', include('companies.urls')),
    url(r'^after-sales-service/', include('after_sales_service.urls')),
    url(r'^products/', include('products.urls')),
    #url(r'^api/', include('api.urls')),
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')), 
    url(r'^rest-auth/', include('rest_auth.urls')), 
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'), 
    url(r'^api-token-refresh/', 'rest_framework_jwt.views.refresh_jwt_token'),
]
