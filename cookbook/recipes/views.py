from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.views.generic import ListView

from .models import Recipe

# Create your views here.
class Recipes(ListView):
    model = Recipe
