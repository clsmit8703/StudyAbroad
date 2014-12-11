from django.conf.urls import patterns, url
from django.conf import settings
from apps.berlin import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gisc2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.MainView.as_view()),
    url(r'^aboutus$', views.AboutUsView.as_view()),
    url(r'^profiles$', views.ProfilesView.as_view()),
    url(r'^profiles/(?P<pk>\d+)/$', views.ProfilesDetailView.as_view(), name='student_dview'),
    url(r'^popular_places$', views.Popular_PlacesView.as_view()),
    url(r'^popular_places/(?P<pk>\d+)/$', views.Popular_PlacesDetailView.as_view(), name='popular_places_dview'),
    url(r'^popular_places_map$', views.Popular_Places_MapView.as_view()),
    url(r'^georgia$', views.GeorgiaView.as_view()),
    url(r'^create$', views.Popular_PlacesCreate.as_view()),
    )

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))