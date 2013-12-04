from django.conf.urls import patterns, include, url
from common.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
						url(r'^$',main, name='main'),
                        url(r'^test/$',test, name='test')
    # Examples:
    # url(r'^$', 'zeekim.views.home', name='home'),
    # url(r'^zeekim/', include('zeekim.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
