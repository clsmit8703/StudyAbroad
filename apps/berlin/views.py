from django.shortcuts import render
from django.views import generic

class MainView(generic.TemplateView):
    """Loads the main page"""
    template_name = 'berlin/main.html'