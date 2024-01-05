from django_filters import rest_framework as filters
from .models import Movie


# We create filters for each field we want to be able to filter on
class MovieFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr='icontains')
    type = filters.CharFilter(lookup_expr='icontains')
    release_year = filters.NumberFilter()
    year__gt = filters.NumberFilter(field_name='release_year', lookup_expr='gt')
    year__lt = filters.NumberFilter(field_name='release_year', lookup_expr='lt')
   

    class Meta:
        model = Movie
        fields = ['title', 'type', 'release_year', 'year__gt', 'year__lt']

