from django.db import models

# Create your models here.
class Loja(models.Model):
    cnpj = models.CharField(max_length=14, unique=True, blank=False)
    nome = models.CharField(max_length=30, blank=False)
    dataFundacao = models.DateField(blank=False)
    
    def __str__(self):
        return self.cnpj + " - " + self.nome

class Produto(models.Model):
    lojaPertencente = models.ForeignKey(Loja, on_delete=models.CASCADE, blank=False)
    nome = models.CharField(max_length=100, blank=False)
    quantidade = models.IntegerField()
    ref = models.CharField(max_length=100, blank=False)
    categoria = models.CharField(max_length=100, blank=False)

    def __str__(self):
        return self.lojaPertencente + " - " + self.nome + " - " + self.quantidade + " - " + self.ref + " - " + self.categoria