## GCloud Girls - Projeto final Luiza Code #3

#### Sobre o projeto:

A GCloud Girls é uma aplicação web que surgiu em 2021 como resultado do projeto integrador do curso de programação web oferecido pelo Programa Luiza Code #3, uma ação entre a Google e a Luiza Labs para formação em tecnologia exclusiva para mulheres.

Foi criado um controlador de estoque para um marketplace, associando empresa e vendedores;
A empresa consegue enviar o produto, ver e atualizar as quantidades, excluir o produto, tudo vinculado ao nome da loja e CNPJ. 
Uma facilidade para a empresa.


##### Público alvo

Pessoas jurídicas interessadas em cadastrar seus produtos para acompanhar a movimentação da sua loja.


##### Metodologia

Os produtos cadastrados ficam disponíveis no sistema para acesso de quantidade e itens disponíveis.

Foi utilizado Django, SQLite, Python, Docker.

##### Como acessar o projeto:

##### No GitHub:
1 - Após clonar o projeto, entrem na pasta raíz e executem este comando: python -m venv venv. Ele serve pra instalar algumas dependências que vamos precisar e também algumas variáveis locais. Importante: Caso seu PC tenha os dois pythons (2 e 3) especifiquem que é o python 3 e o comando vai ficar assim: python3 -m venv venv

2 - Depois vá até a pasta venv/Scripts  e executem o arquivo activate. Nas que usam Linux, só botar activate que é sucesso. Nas que usam Windows (mais especificadamente o power shell) coloque ./activate

3 - Volte a pasta raíz e execute o comando pip install Django. Este comando serve para instalar o Django pelo pip

4 - Na mesma pasta, execute o comando python 
manage.py
 runserver

5 - Pronto. Já estará rodando no localhost:8000

##### No Docker hub:
1 - Acessar o link do projeto:
https://hub.docker.com/r/sammarabn/app-magalu-docker-python

2 – Fazer o pull do projeto no Docker

3 - Rodar as imagens no Docker

##### Desenvolvedoras: 
Grupo 8:
##### [Ana Verônica](https://github.com/Anaveronica3001)
##### [Karolina Queiroz](https://github.com/karolinaq20)
##### [Rachel Carvalho](https://github.com/RachCarvalho)
##### [Sammara Nunes](https://github.com/sammarabn)
