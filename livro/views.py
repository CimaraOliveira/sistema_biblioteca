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

class livros_list(ListView):
    template_name = "livro/livros_list.html"
    model = Livro
    context_object_name = "object_list"

class livros_confirm_delete(DeleteView):
    model = Livro
    template_name = 'livro/livros_confirm_delete.html'
    success_url = reverse_lazy('livro:livros_list')

class livro_update(UpdateView):
    template_name = "livro/livro_update.html"
    model = Livro
    fields = '__all__'
    success_url = reverse_lazy('livro:livros_list')


