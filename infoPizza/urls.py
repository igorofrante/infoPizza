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
    path('cardapio/pizza/view/<int:id>', views.cardapioPizzaView),
    path('cardapio/pizza/form/', views.cardapioPizzaInsert, name='cardapioPizzaInsert'),
    path('cardapio/pizza/form/<int:id>', views.cardapioPizzaUpdate, name='cardapioPizzaUpdate'),
    path('cardapio/pizza/delete/<int:id>', views.cardapioPizzaDestroy),
    path('cardapio/bebida/', views.cardapioBebidaIndex),
    path('cardapio/bebida/view/<int:id>', views.cardapioBebidaView),
    path('cardapio/bebida/form/', views.cardapioBebidaInsert, name='cardapioBebidaInsert'),
    path('cardapio/bebida/form/<int:id>', views.cardapioBebidaUpdate, name='cardapioBebidaUpdate'),
    path('cardapio/bebida/delete/<int:id>', views.cardapioBebidaDestroy),
    path('cliente/', views.clienteIndex),
    path('cliente/view/<int:id>', views.clienteView),
    path('cliente/form/', views.clienteInsert),
    path('cliente/form/<int:id>', views.clienteUpdate),
    path('cliente/delete/<int:id>', views.clienteDestroy),
    path('pedidos/', views.pedidosIndex),
    path('pedidos/form/', views.pedidosInsert, name='pedidosInsert'),
    path('pedidos/ajax/tamanhos', views.load_tamanhos, name='ajax_load_tamanhos'),
    path('pedidos/ajax/preco', views.load_preco),
    path('pedidosUpdate/<int:id>', views.pedidosUpdate, name='pedidosUpdate'),
    path('pedidos/delete/<int:id>', views.pedidoDestroy),

]
