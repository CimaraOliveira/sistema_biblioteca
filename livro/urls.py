from django.urls import path
from . import views

app_name = 'livro'

urlpatterns = [

   path('', views.adicionar_create.as_view(), name='adicionar'),
   path('livros_list/', views.livros_list.as_view(), name='livros_list'),
   path('livro_update/<int:pk>/', views.livro_update.as_view(), name='livro_update'),
   path('livros_confirm_delete/<int:pk>/', views.livros_confirm_delete.as_view(), name='livros_confirm_delete'),



]