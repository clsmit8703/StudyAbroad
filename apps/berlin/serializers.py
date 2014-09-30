from apps.berlin import models
from rest_framework import serializers
from rest_framework_gis import serializers as geoserializers


class UnitSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Student
        fields = ('id', 'first_name', 'last_name', 'major')

