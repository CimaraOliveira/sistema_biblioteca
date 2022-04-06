from .models import Livro
from django import forms

class LivrosModelForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = '__all__'