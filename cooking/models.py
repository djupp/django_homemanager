from django.db import models
from core.models import Good, Measurement


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    ingredients = models.ManyToManyField(Good, through="Ingredient",
                                         through_fields=('recipe', 'good'))
    link = models.URLField()


class Ingredient(models.Model):
    good = models.ForeignKey(Good)
    recipe = models.ForeignKey(Recipe)
    amount = models.DecimalField(max_digits=4, decimal_places=1)
    measurement = models.ForeignKey(Measurement)


class Meal(models.Model):
    servings = models.IntegerField(verbose_name="Number of Servings")
