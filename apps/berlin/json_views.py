from apps.berlin import models, serializers
from rest_framework import generics
import django_filters



class IntegerListFilter(django_filters.Filter):
    def filter(self, qs, value):
        if value not in (None, ' '):
            integers = [int(v) for v in value.split(',')]
            return qs.filter(**{'{}__{}'.format(self.name, self.lookup_type): integers})
        return qs

class MarkerFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Student
        fields = ['id', 'first_name', 'last_name', 'major']

class UserCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Student.objects.all()
    serializer_class = serializers.UnitSerializer
    filter_class = MarkerFilter


class MapFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Map
        fields =['id','geom']

class CountyCollection(generics.ListAPIView):
    queryset = models.Map.objects.all()
    serializer_class = serializers.MapSerializer
    filter_class = MapFilter