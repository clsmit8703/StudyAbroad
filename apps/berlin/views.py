from django.views import generic
from apps.berlin import models
from apps.berlin.forms import Popular_PlacesForm


class MainView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'berlin/main.html'

class AboutUsView(generic.TemplateView):
    template_name = 'berlin/aboutus.html'

class ProfilesView(generic.ListView):
    model = models.Student
    template_name = 'berlin/profiles.html'

class ProfilesDetailView(generic.TemplateView):
    template_name = "berlin/student_detail.html"

    def get_context_data(self, **kwargs):
        """Adding images to context"""
        context = super(ProfilesDetailView, self).get_context_data()
        data = models.Student.objects.filter(pk=kwargs['pk']).first()
        context['student'] = data
        return context

class Popular_PlacesView(generic.ListView):
    model = models.Popular_Places
    template_name = 'berlin/popular_places.html'

class Popular_Places_MapView(generic.TemplateView):
    """Loads the map page"""
    template_name = 'berlin/popular_places_map.html'

class GeorgiaView(generic.TemplateView):
    """Loads the map page"""
    template_name = 'berlin/georgia.html'

class Popular_PlacesDetailView(generic.TemplateView):
    template_name = "berlin/popular_places_detail.html"

    def get_context_data(self, **kwargs):
        """Adding images to context"""
        context = super(Popular_PlacesDetailView, self).get_context_data()
        data = models.Popular_Places.objects.filter(pk=kwargs['pk']).first()
        context['place'] = data
        return context

class Popular_PlacesCreate(generic.edit.FormView):
    template_name = 'berlin/create.html'
    form_class = Popular_PlacesForm
    success_url = '/'
