import django_filters
from .models import BlogPost


class BlogPostFilter(django_filters.FilterSet):

    created_after = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='date__gte'
    )

    created_before = django_filters.DateFilter(
        field_name='created_at',
        lookup_expr='date__lte'
    )

    class Meta:
        model = BlogPost
        fields = [
            'created_after',
            'created_before'
        ]