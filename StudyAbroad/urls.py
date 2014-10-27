from django.conf.urls import patterns, include, url
from django.contrib.gis import admin
admin.autodiscover()

extra_patterns = patterns('',
                          url(r'^', include('apps.berlin.api_urls'), name='berlin'),
                          )

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StudyAbroad.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'berlin/', include('apps.berlin.urls', namespace='berlin')),
    url(r'api/v1/', include(extra_patterns, namespace='api')),
)
