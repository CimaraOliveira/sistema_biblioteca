from django.urls import path
from . import views

app_name = 'livro'

urlpatterns = [

   path('', views.adicionar_create.as_view(), name='adicionar_create'),


]