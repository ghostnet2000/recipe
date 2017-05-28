from django.shortcuts import render

from django.db.models.functions import Lower

from rest_framework import viewsets, generics

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from . import models
from . import serializers
from .form import RecipeForm

def index(request):
    all_recipes = models.Recipe.objects.all()

    return render(request, 'index.html', {'all_recipes': all_recipes})

def detail(request, recipe_id):
    recipe = models.Recipe.objects.get(pk=recipe_id)
    
    return render(request, 'detail.html', {'recipe': recipe })

def delete_recipe(request, recipe_id):
    recipe = models.Recipe.objects.get(pk=recipe_id)
    recipe.delete()
    
    all_recipes = models.Recipe.objects.all()
    return render(request, 'index.html', {'all_recipes': all_recipes})



def create(request):
    """ create Recipe.

        Keyword arguments:
        request -
    """
    print "called"

    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES or None)
        if form.is_valid():
            recipe = form.save(commit=False)

            print request

            recipe.save()
            all_recipes = models.Recipe.objects.all()
            return render(request, 'index.html', {'all_recipes': all_recipes})

    else:
        form = RecipeForm()

    context = {
        "form": form,
    }

    return render(request, 'create.html', {'form': form})
"""
def detail(request, recipe_id):
    recipe = get_object_or_404(models.Recipe, pk=recipe_id)
    return render(request, 'detail.html', {'recipe': recipe})
"""

# API
class RecipeViewSet(viewsets.ModelViewSet):

    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer


class SearchView(generics.ListAPIView):
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        parameter = self.request.GET.get('q', default='')
        return models.Recipe.objects.filter(title__icontains=parameter)

class ByTagView(generics.ListAPIView):
    serializer_class = serializers.RecipeSerializer

    def get_queryset(self):
        tag_id = self.request.GET.get('id', default='')
        return models.Tag.objects.get(pk=tag_id).recipe_set.all()

    def list(self, request):
        tag_id = request.GET.get('id', default='')
        queryset = self.get_queryset()
        serializer = serializers.RecipeSerializer(queryset, many=True)
        response_data = {
            'tag_name': models.Tag.objects.get(pk=tag_id).name,
            'recipes': serializer.data
        }
        return Response(response_data)