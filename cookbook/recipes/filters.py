import django_filters
from django_filters import ModelMultipleChoiceFilter

from .models import Recipe,Kitchen

class RecipeFilter(django_filters.FilterSet):
    class Meta:
        model = Recipe
        fields = {
            "name": ["icontains"],
            "kitchen": [ "exact"] ,
            "number_of_persons": ["exact"] ,


        }

