from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Livro
from .forms import LivrosModelForm
from django.urls import reverse_lazy

class adicionar_create(CreateView):
    template_name = "livro/adicionar_create.html"
    model = Livro
    form_class = LivrosModelForm
    success_url = reverse_lazy('livro:livros_list')



