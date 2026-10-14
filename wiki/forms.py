from django import forms
from wiki.models import Pagina, Categoria

class PaginaForm(forms.ModelForm):
    class Meta:
        model = Pagina
        fields = ['titulo', 'categoria', 'tags', 'conteudo_atual']

        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Laboratório de Redes'}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'conteudo_atual': forms.Textarea(attrs={'class': 'form-control', 'rows': 10, 'placeholder': 'Use Markdown para formatar...'}),
        }



# class CategoriaForm(forms.ModelForm):
#     class Meta:
#         model = Categoria
#         fields = ['nome', 'descricao']
