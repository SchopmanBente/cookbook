from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, DetailView

from .models import Recipe
from .filters import RecipeFilter

# Create your views here.
class RecipeListView(ListView):
    model = Recipe
    template_name =  "recipes/recipe_list.html"

    def get_context_data(self,  **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = RecipeFilter(self.request.GET, queryset=self.get_queryset())
        return context

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_detail.html"