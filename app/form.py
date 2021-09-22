from django.forms import ModelForm
from app.models import Loja, Produto

# Create the form class.
class LojaForm(ModelForm):
    class Meta:
        model = Loja
        fields = ['cnpj', 'nome', 'dataFundacao']

class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['lojaPertencente', 'nome', 'quantidade', 'ref', 'categoria']