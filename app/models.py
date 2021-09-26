from django.db import models

# Create your models here.


class Loja(models.Model):
    cnpj = models.CharField(max_length=14, unique=True, blank=False)
    nome = models.CharField(max_length=30, blank=False)
    dataFundacao = models.DateField(blank=False)

    def __str__(self):
        return self.cnpj + " - " + self.nome


class Categoria(models.Model):
    lojaPertencente = models.ForeignKey(
        Loja, on_delete=models.CASCADE, blank=False)
    nome = models.CharField(max_length=50, blank=False, unique=True)

    def __str__(self):
        return self.nome


class Produto(models.Model):