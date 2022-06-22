from django.urls import path

from .views import Recipes, RecipeView

app_name = 'recipes'

urlpatterns = [
    path('', Recipes.as_view(), name="index"),
    path("recipes/<int:pk>", RecipeView.as_view(), name="detail")
]