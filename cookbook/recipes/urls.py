from django.urls import path

from .views import Recipes

app_name = 'recipes'

urlpatterns = [
    path('', Recipes.as_view(), name="index"),
]