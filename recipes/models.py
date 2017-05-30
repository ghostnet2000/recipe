from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_delete

class Tag(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Recipe(models.Model):
    title = models.CharField(max_length=255)
    instructions = models.TextField()
    ratings = models.DurationField(blank=True, null=True)
    servings = models.CharField(blank=True, max_length=255)
    prep_time = models.DurationField(blank=True, null=True)
    cooking_time = models.DurationField(blank=True, null=True)
    ingredients = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='static/media/Images', default="Images/none.png");

    def __str__(self):
        return self.title

class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    recipe = models.ForeignKey(Recipe, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

