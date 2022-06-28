from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Recipe

# Create your views here.
class Recipes(ListView):
    model = Recipe

def get(request, pk, format=None):
    recipe = Recipe.objects.get(id=pk)
    ingredients = recipe.ingredients.all()
    necessities = recipe.necessities.all()
    return render(request, "recipes/recipe_detail.html",
                  {"name": recipe.name,
                   "time": recipe.time,
                   "number_of_persons": recipe.number_of_persons,
                   "kitchen": recipe.kitchen,
                   "necessities": necessities,
                   "ingredients": ingredients,
                   "preparation": recipe.preparation,
                   })