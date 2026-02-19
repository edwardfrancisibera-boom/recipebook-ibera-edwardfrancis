from django.shortcuts import render
from .models import Recipe
from django.views.generic import ListView, DetailView

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'
