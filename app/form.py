from django.forms import ModelForm
from app.models import Categoria, Loja, Produto

# Create the form class.
class LojaForm(ModelForm):
    class Meta:
        model = Loja
        fields = ['cnpj', 'nome', 'dataFundacao']

class CategoriaForm(ModelForm):

    class Meta:
        model = Categoria
        fields = ['lojaPertencente', 'nome']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['lojaPertencente', 'categoria', 'nome', 'quantidade', 'descricao']