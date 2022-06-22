from django.urls import path

from .views import RecipesView, RecipeView

app_name = 'recipes'

urlpatterns = [
    path('', RecipesView.as_view(), name="index"),
    path("recipes/<int:pk>",RecipeView.as_view(), name="detail")
]