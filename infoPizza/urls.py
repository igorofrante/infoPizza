"""infoPizza URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('cardapio/', views.cardapioIndex),
    path('cardapio/pizza/', views.cardapioPizzaIndex),
    path('cardapioPizzaInsert/', views.cardapioPizzaInsert, name='cardapioPizzaInsert'),
    path('cardapioPizzaUpdate/<int:id>', views.cardapioPizzaUpdate, name='cardapioPizzaUpdate'),
    path('cardapio/pizza/delete/<int:id>', views.cardapioPizzaDestroy),
    path('cardapio/bebida/', views.cardapioBebidaIndex),
    path('cardapioBebidaInsert/', views.cardapioBebidaInsert, name='cardapioBebidaInsert'),
    path('cardapioBebidaUpdate/<int:id>', views.cardapioBebidaUpdate, name='cardapioBebidaUpdate'),
    path('cardapio/bebida/delete/<int:id>', views.cardapioBebidaDestroy),
    path('pedidos/',views.pedidosIndex),
    path('pedidos/insert',views.pedidosInsert),
    path('pedidos/hr/tamanho_dropdown_list_options', views.load_tamanhos, name='ajax_load_tamanhos'),
    path('pedidos/hr/preco', views.load_preco),
    
]
