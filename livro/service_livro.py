from rest_framework import viewsets
from .models import Livro
from .serializer import LivroSerializer

class listarLivro(viewsets.ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

