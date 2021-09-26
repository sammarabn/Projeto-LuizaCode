"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import allCategories, allProducts, allStores, createCategories, deleteCategories, editCategories, formCategories, home, form, create, updateCategories, view, edit, update, delete, formProducts, createProducts, updateProducts, viewCategories, viewProducts, editProducts, deleteProducts

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    
    path('form/', form, name='form'),
    path('allStores/', allStores, name='allStores'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>/', update, name='update'),
    path('delete/<int:pk>/', delete, name='delete'),

    path('allCategories/', allCategories, name='allCategories'),
    path('formCategories/<int:pk>/', formCategories, name='formCategories'),
    path('createCategories/', createCategories, name='createCategories'),
    path('viewCategories/<int:pkc>/', viewCategories, name='viewCategories'),
    path('editCategories/<int:pkc>/', editCategories, name='editCategories'),
    path('updateCategories/<int:pkc>/', updateCategories, name='updateCategories'),
    path('deleteCategories/<int:pkc>/', deleteCategories, name='deleteCategories'),
    
    path('allProducts/', allProducts, name='allProducts'),
    path('formProducts/<int:pk>/', formProducts, name='formProducts'),
    path('createProducts/', createProducts, name='createProducts'),
    path('viewProducts/<int:pkp>/', viewProducts, name='viewProducts'),
    path('editProducts/<int:pkp>/', editProducts, name='editProducts'),
    path('updateProducts/<int:pkp>/', updateProducts, name='updateProducts'),
    path('deleteProducts/<int:pkp>/', deleteProducts, name='deleteProducts')
]
