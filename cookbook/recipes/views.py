from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from django.views.generic.detail import DetailView
from .models import Recipe

# Create your views here.
class RecipesView(ListView):
    model = Recipe

class RecipeView(DetailView):
    model = Recipe
    context_object_name = "detail"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Recipe"] = Recipe.object
        return context