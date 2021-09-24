from django.shortcuts import render, redirect
from app.form import LojaForm, ProdutoForm
from app.models import Loja, Produto

# Create your views here.
def home(request):
    data ={}
    data['db'] = Loja.objects.all().values("id","cnpj", "nome")
    return render(request, 'index.html', {"lojas": data})

def form(request):
    data ={}
    data['form'] = LojaForm()
    return render(request, 'form.html', data)

def create(request):
    form = LojaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Loja.objects.get(pk=pk)
    data['dbp'] = Produto.objects.filter(lojaPertencente = pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Loja.objects.get(pk=pk)
    data['form'] = LojaForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Loja.objects.get(pk=pk)
    form = LojaForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Loja.objects.get(pk=pk)
    db.delete()
    return redirect('home')

def formProducts(request, pk):
    data = {}
    data['db'] = Loja.objects.get(pk=pk)
    data['formProducts'] = ProdutoForm
    return render(request, 'formProducts.html', data)

def createProducts(request):
    formProduct = ProdutoForm(request.POST or None)
    print(formProduct)
    if formProduct.is_valid():
        formProduct.save()
        return redirect('home')

def viewProducts(request, pkl, pkp):
    data = {}
    data['db'] = Loja.objects.get(pk=pkl)
    data['dbp'] = Produto.objects.get(pk=pkp)
    return render(request, 'viewProducts.html', data)

def editProducts(request, pkp):
    data = {}
    data['dbp'] = Produto.objects.get(pk=pkp)
    data['formProducts'] = ProdutoForm(instance=data['dbp'])
    return render(request, 'formProducts.html', data)

def updateProducts(request, pkp):
    data = {}
    data['dbp'] = Produto.objects.get(pk=pkp)
    form = ProdutoForm(request.POST or None, instance=data['dbp'])
    if form.is_valid():
        form.save()
        return redirect('home')

def deleteProducts(request, pkp):
    db = Produto.objects.get(pk=pkp)
    db.delete()
    return redirect('home')
