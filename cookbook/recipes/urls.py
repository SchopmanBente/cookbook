from django.urls import path

from .views import Recipes, get

app_name = 'recipes'

urlpatterns = [
    path('', Recipes.as_view(), name="index"),
    path("recipes/<int:pk>", get, name="detail")
]