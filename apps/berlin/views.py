from django.shortcuts import render
from django.views import generic

class MainView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'berlin/main.html'

class AboutUsView(generic.TemplateView):
    template_name = 'berlin/aboutus.html'

class ProfilesView(generic.TemplateView):
    template_name = 'berlin/profiles.html'