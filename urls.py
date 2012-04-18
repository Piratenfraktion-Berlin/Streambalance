from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	(r'^icecast_balancer/', include('icecast_balancer.urls')),
    # Example:
    # (r'^loadbalancer/', include('loadbalancer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
    (r'^$', 'frontpage.views.frontpage'),
)
