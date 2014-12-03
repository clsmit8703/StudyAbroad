from django.contrib.gis import forms
from django.contrib.gis.forms.widgets import BaseGeometryWidget


class Popular_PlacesForm(forms.Form):
    name = forms.CharField()
    desc = forms.CharField(max_length=100)
    type = forms.CharField(max_length=30)
    #geom = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 800, 'map_height': 500}))
    #geom =forms.PointField(widget=BaseGeometryWidget(attrs={'map_width': 100}))
    Latitude = forms.DecimalField(max_digits=10, decimal_places=6)
    Longitude = forms.DecimalField(max_digits=10, decimal_places=6)
