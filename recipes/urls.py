from django.conf.urls import url, include
from django.conf.urls.static import static
from django.conf import settings 
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
  #url(r'$', views.index),
  url(r'^$', views.index, name='index'),
  url(r'^create/$', views.create, name='create'),
  url(r'^(?P<recipe_id>[0-9]+)/detail/$', views.detail, name='detail'),
  url(r'^(?P<recipe_id>[0-9]+)/delete_recipe/$', views.delete_recipe, name='delete_recipe'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)