from django.test.client import Client
from django.test import TestCase
from .models import Loja
from .views import home, create, view
from datetime import date
from django.urls import reverse

class TestLojaViews(TestCase):

    def setUp(self):
        self.lojas_inseridas = []
        self.lojas_inseridas.append(Loja.objects.create(cnpj=12345678910234, nome="Lojinha", dataFundacao=date(2021,9,23)))
        self.lojas_inseridas.append(Loja.objects.create(cnpj=12345678910456, nome="Lojona", dataFundacao=date(2021,9,23)))

    def test_listar_lojas(self):
        c = Client()

        str_url = reverse("home")
        resposta = c.get(str_url)

        dados_resposta = resposta.context

        lst_lojas_resposta = dados_resposta["lojas"]


        for loja_resposta in lst_lojas_resposta:
            
            encontrou = False
            for loja_inserida in self.lojas_inseridas:
                if int(loja_resposta["id"]) == loja_inserida.id:
                    encontrou = True
                    self.assertEqual(loja_resposta["nome"],loja_inserida.nome, "Nome inesperado ao listar loja")
            self.assertTrue(encontrou, f"A loja {loja_resposta} não foi encontrada")
        self.assertEqual(len(self.lojas_inseridas), len(lst_lojas_resposta), "O número de lojas inseridas é diferente do obtido na resposta!")
    
""" def test_inserir_loja(self):
        c = Client()

        str_url = reverse("create")
        c.post(str_url, {"cnpj":12345678910234, "nome":"Lojinha", "dataFundacao":"2021-9-23"})

        lst_loja_lojinha = Loja.objects.filter(cnpj=12345678910234)

        self.assertNotEquals(0,len(lst_loja_lojinha), "Não foi possível encontrar a loja inserida")
        self.assertEquals(1,len(lst_loja_lojinha), "Loja foi inserida mais de uma vez")"""
