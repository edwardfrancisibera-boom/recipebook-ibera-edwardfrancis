from django import forms
from .models import Recipe, RecipeImage

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        excluded = ["author"]

class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = RecipeImage
        excluded = ["recipe"]