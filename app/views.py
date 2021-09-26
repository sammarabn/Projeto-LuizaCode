from django.shortcuts import render, redirect
from app.form import CategoriaForm, LojaForm, ProdutoForm
from app.models import Categoria, Loja, Produto

# Create your views here.


def home(request):
    return render(request, 'index.html')


def allStores(request):
    data = {}
    data['db'] = Loja.objects.all()
    return render(request, 'allStores.html', data)


def form(request):
    data = {}
    data['form'] = LojaForm()
    return render(request, 'form.html', data)


def create(request):
    form = LojaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('allStores')


def view(request, pk):
    data = {}
    data['db'] = Loja.objects.get(pk=pk)
    data['dbp'] = Produto.objects.filter(lojaPertencente=pk)
    data['dbc'] = Categoria.objects.filter(lojaPertencente=pk)
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
        return render(request, 'form.html', data)


def delete(request, pk):
    db = Loja.objects.get(pk=pk)
    db.delete()
    return redirect('allStores')


def allCategories(request):
    data = {}
    data['db'] = Categoria.objects.all()
    return render(request, 'allCategories.html', data)


def formCategories(request, pk):
    data = {}
    data['db'] = Loja.objects.get(pk=pk)
    data['formCategories'] = CategoriaForm()
    return render(request, 'formCategories.html', data)


def createCategories(request):
    formCategory = CategoriaForm(request.POST or None)
    print(formCategory)
    if formCategory.is_valid():
        formCategory.save()
        return redirect('allCategories')


def viewCategories(request, pkc):
    data = {}
    data['dbc'] = Categoria.objects.get(pk=pkc)
    return render(request, 'viewCategories.html', data)


def editCategories(request, pkc):
    data = {}
    data['dbc'] = Categoria.objects.get(pk=pkc)
    data['formCategories'] = CategoriaForm(instance=data['dbc'])
    return render(request, 'formCategories.html', data)


def updateCategories(request, pkc):
    data = {}
    data['dbc'] = Categoria.objects.get(pk=pkc)
    form = CategoriaForm(request.POST or None, instance=data['dbc'])
    if form.is_valid():
        form.save()
        return render(request, 'formCategories.html', data)


def deleteCategories(request, pkc):
    db = Categoria.objects.get(pk=pkc)
    db.delete()
    return redirect('allCategories')


def allProducts(request):
    data = {}
    data['db'] = Produto.objects.all()
    return render(request, 'allProducts.html', data)


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
        return redirect('allProducts')


def viewProducts(request, pkp):
    data = {}
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
        return render(request, 'viewProducts.html', data)


def deleteProducts(request, pkp):
    db = Produto.objects.get(pk=pkp)
    db.delete()
    return redirect('allProducts')
