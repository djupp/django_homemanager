# from django.shortcuts import render
from django.views.generic import ListView, DetailView
from cooking.models import Recipe
from cooking.models import Ingredient


class RecipesList(ListView):

    model = Recipe
    context_object_name = "recipes"


class RecipeDetail(DetailView):
    context_object_name = "recipe"
    model = Recipe
    template_name = "recipe_detail.html"

    def get_context_data(self, **kwargs):
        context = super(RecipeDetail, self).get_context_data(**kwargs)
        context['ingredients'] = Ingredient.objects.filter(
            recipe=kwargs['object'])
