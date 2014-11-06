from django.conf.urls import patterns, include, url
from apps.berlin import json_views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^berlin$', json_views.StudentCollection.as_view(), name='berlin'),
    url(r'^georgia$', json_views.GeorgiaCollection.as_view(), name='georgia'),
    url(r'^popular_places$', json_views.Popular_PlacesCollection.as_view(), name='popular_places'),
    )