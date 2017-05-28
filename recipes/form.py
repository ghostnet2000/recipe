from django import forms

from .models import Recipe


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
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

