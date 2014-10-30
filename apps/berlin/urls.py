from django.conf.urls import patterns, url

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
    )