from django import forms
from .models import Imovel, Vendedor

class ImovelForm(forms.ModelForm):

    class Meta:
        model = Imovel
        fields = ('endereco', 'valor', 'bairro', 'anuncio', 'imagem', 'vendedor')


class VendedorForm(forms.ModelForm):

    class Meta:
        model = Vendedor
        fields = ('nome', 'sobrenome', 'telefone')

class PesquisaForm(forms.ModelForm):
    pesquisa = forms.CharField(label='Pesquisa')
