from rest_framework import serializers
from . import models


class RecipeSerializer(serializers.ModelSerializer):

    image = serializers.ImageField(max_length=None,use_url=True)

    def create(self, validated_data):

        # Create Recipe without ingredients or tags
        tags_data = validated_data.pop('title')
        recipe = models.Recipe.objects.create(**validated_data)

        return recipe

    def update(self, instance, validated_data):
        
        instance.title = validated_data.get('title')
        instance.instructions = validated_data.get('instructions')
        instance.servings = validated_data.get('serve_with')
        instance.ratings = validated_data.get('ratings')
        instance.prep_time = validated_data.get('prep_time')
        instance.cooking_time = validated_data.get('cooking_time')
        instance.ingredients = validated_data.get('notes')
        instance.image = validated_data.get('image')

        instance.save()

        return instance

    class Meta:
        model = models.Recipe
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