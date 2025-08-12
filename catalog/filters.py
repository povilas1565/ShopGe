import django_filters
from .models import Product


class ProductFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='filter_q', label='Поиск')
    category = django_filters.CharFilter(field_name='category__slug')
    is_active = django_filters.BooleanFilter()

    class Meta:
        model = Product
        fields = ['q', 'category', 'is_active']

    def filter_q(self, queryset, name, value):
        return queryset.filter(title__icontains=value)
