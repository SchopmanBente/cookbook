from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Recipe

# Create your views here.
class Recipes(ListView):
    model = Recipe

class RecipeView(DetailView):
    model = Recipe
    context_object_name = "detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Recipe_name"] = Recipe.name
        return context