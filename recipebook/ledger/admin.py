from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Recipe, RecipeIngredient, Ingredient, Profile, RecipeImage

class RecipeIngredientInline(admin.TabularInline):
    model = RecipeIngredient

class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientInline, RecipeImageInLine]

class IngredientAdmin(admin.ModelAdmin):
    model = Ingredient

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class RecipeImageInLine(admin.TabularInline):
    admin = RecipeImage

class UserAdmin(BaseUserAdmin):
    inlines = [ProfileInline,]

admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient, IngredientAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)