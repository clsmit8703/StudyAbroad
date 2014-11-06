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
        fields = ['id', 'first_name', 'last_name', 'major', 'school', 'AM_class','PM_class']

class StudentCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Student.objects.all()
    serializer_class = serializers.StudentSerializer
    filter_class = MarkerFilter


class Popular_PlacesFilter(django_filters.FilterSet):
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Popular_Places
        fields = ['id','geom']

class Popular_PlacesCollection(generics.ListAPIView):
    queryset = models.Popular_Places.objects.all()
    serializer_class = serializers.Popular_PlacesSerializer
    filter_class = Popular_PlacesFilter


class GeorgiaFilter(django_filters.FilterSet):
    """Json_view for Georgia Model"""
    id = IntegerListFilter(name='id', lookup_type='in')

    class Meta:
        model = models.Georgia
        fields = ['name','lat']

class GeorgiaCollection(generics.ListAPIView):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = models.Georgia.objects.all()
    serializer_class = serializers.GeorgiaSerializer
    filter_class = GeorgiaFilter
