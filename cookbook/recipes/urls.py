from django.urls import path

from .views import  RecipeListView, RecipeDetailView

app_name = 'recipes'
urlpatterns = [
    path('', RecipeListView.as_view(), name="index"),
    path("recipes/<int:pk>", RecipeDetailView.as_view(), name="detail")
]