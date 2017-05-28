from django.contrib import admin
from . import models


class RecipeAdmin(admin.ModelAdmin):
    fields = (
        'id',
        'title',
        'instructions',
        'ratings',
        'servings',
        'prep_time',
        'cooking_time',
        'ingredients',
        'image',
    )

# Register your models here.
admin.site.register(models.Recipe, RecipeAdmin)

