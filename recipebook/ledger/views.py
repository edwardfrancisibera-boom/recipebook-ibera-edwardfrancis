from django.shortcuts import render
from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipe_list.html'

class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe_detail.html'

class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_create.html"
    form_class = RecipeForm

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)

class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "recipe_add_image.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy(
            "ledger:recipe_detail", kwargs={"pk": self.object.recipe.pk}
        )

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
