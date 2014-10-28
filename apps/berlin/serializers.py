from apps.berlin import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'first_name', 'last_name', 'major', 'school','AM_class','PM_class')

class MapSerializer(geoserializers.GeoFeatureModelSerializer):
    class Meta:
        model = models.Map
        geo_field = 'geom'
        fields = ('id','name')
