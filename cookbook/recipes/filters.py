import django_filters
from django_filters import MultipleChoiceFilter

from .models import Recipe


class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = {
            "name": ["icontains"],
            "time": ["exact"],
            "kitchen": ["exact"],
            "number_of_persons": ["exact"],
            "ingredients": ["exact"],
            "necessities": ["exact"],
            "preparation": ["icontains"],
        }

