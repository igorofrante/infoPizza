from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.forms import * 
from app.models import *
import logging

# logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
# logging.debug(form)

# Create your views here.

def index(request):
    return render(request,'index.html')

def cardapioIndex (request):
    return render(request, 'cardapio/index.html')

# PIZZA
def cardapioPizzaIndex(request):
    pizzas = Produto.objects.filter(cat__iexact=1) 
    return render(request,'cardapio/pizza/index.html',{'pizzas':pizzas}) 

def cardapioPizzaInsert(request) :
    novaPizza = Produto(cat=1)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=novaPizza, prefix='form')
        form2 = PizzaFormset(request.POST, request.FILES, instance=novaPizza, prefix='form2')
        if form.is_valid() and form2.is_valid():   
            form.save()
            form2.save()
            return redirect('/cardapio/pizza')  
    else:  
        form = ProdutoForm(instance=novaPizza, prefix='form')
        form2 = PizzaFormset(instance=novaPizza, prefix='form2')
    return render(request,'cardapio/pizza/formPizza.html', {'form':form,'form2':form2})  

def cardapioPizzaUpdate(request, id):  
    pizza = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=pizza, prefix='form')
        form2 = PizzaFormset(request.POST, request.FILES, instance=pizza, prefix='form2')
        if form.is_valid() and form2.is_valid():  
            form.save()
            form2.save()
            return redirect('/cardapio/pizza')  
        else:
            return print(form2.errors)
    else:
        form = ProdutoForm(instance=pizza, prefix='form')
        form2 = PizzaFormset(instance=pizza, prefix='form2')
    return render(request, 'cardapio/pizza/formPizza.html', {'form':form,'form2':form2,'pizza':pizza})  

def cardapioPizzaDestroy(request, id):  
    pizza = Produto.objects.get(id=id)  
    pizza.delete()  
    return redirect("/cardapio/pizza")

# BEBIDA
def cardapioBebidaIndex(request) :
    bebidas = Produto.objects.filter(cat__iexact=2)
    return render(request,"cardapio/bebida/index.html", {'bebidas':bebidas}) 

def cardapioBebidaInsert(request) :
    novaBebida = Produto(cat=2)
    if request.method == "POST":
        form = ProdutoForm(request.POST, request.FILES, instance=novaBebida, prefix='form')
        form2 = BebidaFormset(request.POST, request.FILES, instance=novaBebida, prefix='form2')
        if form.is_valid() and form2.is_valid():  
            form.save()
            form2.save()
            return redirect('/cardapio/bebida')  
    else:  
        form = ProdutoForm(instance=novaBebida, prefix='form')
        form2 = BebidaFormset(instance=novaBebida, prefix='form2')
    return render(request,'cardapio/bebida/formBebida.html', {'form':form, 'form2':form2})  

def cardapioBebidaUpdate(request, id):  
    bebida = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST,request.FILES, instance=bebida, prefix='form')
        form2 = BebidaFormset(request.POST,request.FILES, instance=bebida, prefix='form2')
        if form.is_valid() and form2.is_valid():  
            form.save()
            form2.save()
            return redirect('/cardapio/bebida')  
    else:
        form = ProdutoForm(instance=bebida, prefix='form')
        form2 = BebidaFormset(instance=bebida, prefix='form2')
    return render(request, 'cardapio/bebida/formBebida.html', {'form':form,'form2':form2,'bebida':bebida})  

def cardapioBebidaDestroy(request, id):  
    bebida = Produto.objects.get(id=id)  
    bebida.delete()  
    return redirect("/cardapio/bebida")

# PEDIDO
def pedidosIndex(request) :
    pedidos = Pedido.objects.all()
    return render(request,"pedidos/index.html",{'pedidos':pedidos}) 

def pedidosInsert(request) :
    novoPedido = Pedido()
    if request.method == "POST":
        form = PedidoForm(request.POST,request.FILES,instance=novoPedido,prefix='form')
        form2 = PedidoFormset(request.POST,request.FILES,instance=novoPedido,prefix='form2')
        form3 = PedidoFormset(request.POST,request.FILES,instance=novoPedido,prefix='form3')
        if form.is_valid() and form2.is_valid() and form3.is_valid():  
            try:  
                form.save()
                form2.save()
                return redirect('/pedidos')  
            except:  
                pass  
    else:  
        form = PedidoForm(instance=novoPedido,prefix='form')
        form2 = PedidoFormset(instance=novoPedido,prefix='form2')
        form3 = PedidoFormset(instance=novoPedido,prefix='form3')
    return render(request,'pedidos/insert.html',{'form':form,'form2':form2,'form3':form3})  


def load_tamanhos(request):
    produto_id = request.GET.get('produto')
    produto_id = Produto.objects.get(nome=produto_id).id
    tamanhos = Pizza.objects.filter(produto=produto_id)
    return render(request, 'pedidos/hr/tamanho_dropdown_list_options.html', {'tamanhos': tamanhos})