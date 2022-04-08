from django.contrib import admin
from .models import Livro

class LivroAdmin(admin.ModelAdmin):
    list_display = ['nome', 'autor','isbn', 'editora'] #visualizar
    list_filter = ['nome', 'autor'] #filtrando por nome e autor
    list_display_links = ['nome'] #clicavel
    list_per_page = 2 #paginação
    search_fields = ['nome', 'autor'] #pesquisa



admin.site.register(Livro, LivroAdmin)
