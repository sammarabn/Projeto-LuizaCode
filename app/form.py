from django.forms import ModelForm
from app.models import Categoria, Loja

# Create the form class.
class LojaForm(ModelForm):
    class Meta:
        model = Loja
        fields = ['cnpj', 'nome', 'dataFundacao']

class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = ['lojaPertencente', 'nome']

