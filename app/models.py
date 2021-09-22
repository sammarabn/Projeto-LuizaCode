from django.db import models

# Create your models here.
class Loja(models.Model):
    cnpj = models.CharField(max_length=14, unique=True, blank=False)
    nome = models.CharField(max_length=30, blank=False)
    dataFundacao = models.DateField(blank=False)

class Produto(models.Model):
    lojaPertencente = models.ForeignKey(Loja, on_delete=models.CASCADE, blank=False)
    nome = models.CharField(max_length=100, blank=False)
    quantidade = models.IntegerField()
    ref = models.CharField(max_length=100, blank=False)
    categoria = models.CharField(max_length=100, blank=False)