from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StudyAbroad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.berlin.urls', namespace='berlin')),
    url(r'api/v1/', include('apps.berlin.api_urls', namespace='api')),
)
