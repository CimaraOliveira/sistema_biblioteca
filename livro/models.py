from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    editora = models.CharField(max_length=50)
    isbn = models.IntegerField()

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Livro'
