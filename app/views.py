from datetime import datetime,time,timedelta
from django.http import HttpResponse
from django.shortcuts import redirect, render
from app.forms import * 
from app.models import *
import logging

# logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
# logging.debug(form)

# Create your views here.

def index(request):
    pedidoshoje = Pedido.objects.all().count() #filter =today
    return render(request, 'index.html', {'pedidoshoje':pedidoshoje})

def cardapioIndex (request):
    return render(request, 'cardapio/index.html')

# PIZZA
def cardapioPizzaIndex(request):
    pizzas = Produto.objects.filter(cat__iexact=1) 
    return render(request,'cardapio/pizza/index.html',{'pizzas':pizzas}) 

def cardapioPizzaView(request, id):
    pizza = Produto.objects.get(id=id)
    pizzaInfo = ProdutoInfo.objects.filter(produto_id=id)
    return render(request, 'cardapio/pizza/view.html', {'pizza':pizza, 'pizzaInfo':pizzaInfo})

def cardapioPizzaInsert(request) :
    novaPizza = Produto(cat=1)
    if request.method == "POST":
        form = ProdutoForm(request.POST,instance=novaPizza, prefix='form')
        form2 = PizzaFormset(request.POST,instance=novaPizza, prefix='form2')
        if form.is_valid() and form2.is_valid():   
            form.save()
            form2.save()
            return redirect('/cardapio/pizza')  
    else:  
        form = ProdutoForm(instance=novaPizza, prefix='form')
        form2 = PizzaFormset(instance=novaPizza, prefix='form2')
    return render(request,'cardapio/pizza/form.html', {'form':form,'form2':form2})  

def cardapioPizzaUpdate(request, id):  
    pizza = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST,instance=pizza, prefix='form')
        form2 = PizzaFormset(request.POST,instance=pizza, prefix='form2')
        if form.is_valid() and form2.is_valid():  
            form.save()
            form2.save()
            return redirect('/cardapio/pizza')  
        else:
            return print(form2.errors)
    else:
        form = ProdutoForm(instance=pizza, prefix='form')
        form2 = PizzaFormset(instance=pizza, prefix='form2')
    return render(request, 'cardapio/pizza/form.html', {'form':form,'form2':form2,'pizza':pizza})  

def cardapioPizzaDestroy(request, id):  
    pizza = Produto.objects.get(id=id)  
    pizza.delete()  
    return redirect("/cardapio/pizza")

# BEBIDA
def cardapioBebidaIndex(request) :
    bebidas = Produto.objects.filter(cat__iexact=2)
    return render(request,"cardapio/bebida/index.html", {'bebidas':bebidas}) 

def cardapioBebidaView(request, id):
    bebida = Produto.objects.get(id=id)
    bebidaInfo = ProdutoInfo.objects.filter(produto_id=id)
    return render(request, 'cardapio/bebida/view.html', {'bebida':bebida, 'bebidaInfo':bebidaInfo})

def cardapioBebidaInsert(request) :
    novaBebida = Produto(cat=2)
    if request.method == "POST":
        form = ProdutoForm(request.POST,instance=novaBebida, prefix='form')
        form2 = BebidaFormset(request.POST,instance=novaBebida, prefix='form2')
        if form.is_valid() and form2.is_valid():  
            form.save()
            form2.save()
            return redirect('/cardapio/bebida')  
    else:  
        form = ProdutoForm(instance=novaBebida, prefix='form')
        form2 = BebidaFormset(instance=novaBebida, prefix='form2')
    return render(request,'cardapio/bebida/form.html', {'form':form, 'form2':form2})  

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
    return render(request, 'cardapio/bebida/form.html', {'form':form,'form2':form2,'bebida':bebida})  

def cardapioBebidaDestroy(request, id):  
    bebida = Produto.objects.get(id=id)  
    bebida.delete()  
    return redirect("/cardapio/bebida")

#CLIENTE
def clienteIndex(request):
    clientes = Cliente.objects.all()
    return render(request, 'cliente/index.html', {'clientes':clientes})

def clienteView(request,id):
     cliente = Cliente.objects.get(id=id)
     return render(request, 'cliente/view.html', {'cliente':cliente})

def clienteInsert(request):
    if request.method == "POST":
        form = clienteForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('/cliente/')  
    else:  
        form = clienteForm()
    return render(request,'cliente/form.html', {'form':form})  

def clienteUpdate(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        form = clienteForm(request.POST, instance=cliente)
        if form.is_valid():  
            form.save()
            return redirect('/cliente/')  
    else:  
        form = clienteForm(instance=cliente)
    return render(request,'cliente/form.html', {'form':form})  

def clienteDestroy(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/cliente/')

# PEDIDO
def pedidosIndex(request) :
    pedidos = Pedido.objects.all()
    return render(request,"pedidos/index.html",{'pedidos':pedidos}) 

def indexContPedidos(request):
    # if datetime.now().time()> time(23,59):
    #     startdate =  datetime.now()
    #     startdate = startdate.replace(hour=18,minute=0,second=0)
    #     enddate = startdate + timedelta(days=1)
    #     enddate = enddate.replace(hour=5,minute=0,second=0)
    # else:
    #     startday =  datetime.now() - timedelta(days=1)
    #     startday = startday.replace(hour=18,minute=0,second=0)
    #     enddate = datetime.now()
    #     endday= enddate.replace(hour=5,minute=0,second=0) 
    pedidoshoje = Pedido.objects.all().count() #filter =today
    return render(request, 'index.html', {'pedidoshoje':pedidoshoje})

def pedidosInsert(request) :
    novoPedido = Pedido()
    if request.method == "POST":
        form = PedidoForm(request.POST,instance=novoPedido, prefix='form')
        form2 = PedidoPizzaFormset(request.POST,request.FILES, instance=novoPedido, prefix='form2')
        form3 = PedidoBebidaFormset(request.POST,request.FILES, instance=novoPedido, prefix='form3')

        if form.is_valid() and form2.is_valid() and form3.is_valid():  
            try:  
                form.save()
                form2.save()
                form3.save()
                return redirect('/pedidos')  
            except:  
                pass  
    else:  
        form = PedidoForm(instance=novoPedido,prefix='form')
        form2 = PedidoPizzaFormset(instance=novoPedido,prefix='form2')
        form3 = PedidoBebidaFormset(instance=novoPedido,prefix='form3')
    return render(request,'pedidos/form.html', {'form':form, 'form2':form2, 'form3':form3})  

def pedidosUpdate(request, id):
    pedido = Pedido.objects.get(id=id)
    if request.method == "POST":
        form = PedidoForm(request.POST,instance=pedido, prefix='form')
        form2 = PedidoPizzaFormset(request.POST,instance=pedido, prefix='form2')
        form3 = PedidoBebidaFormset(request.POST,instance=pedido, prefix='form3')
        logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
        logging.debug(request.POST)
        if form.is_valid() and form2.is_valid() and form3.is_valid():  
            try:  
                form.save()
                form2.save()
                form3.save()
                return redirect('/pedidos')  
            except:  
                pass  
    else:  
        form = PedidoForm(instance=pedido,prefix='form')
        form2 = PedidoPizzaFormset(instance=pedido,prefix='form2')
        form3 = PedidoBebidaFormset(instance=pedido,prefix='form3')
    return render(request,'pedidos/form.html',{'form':form, 'form2':form2, 'form3':form3,'pedido':pedido})
        
def load_tamanhos(request):
    produto_id = request.GET.get('produto')
    tamanhos = ProdutoInfo.objects.filter(produto=produto_id)
    return render(request, 'pedidos/ajax/tamanhos.html', {'tamanhos': tamanhos})

def load_tamanho(request):
    produto_id = request.GET.get('produto')
    pedido_id = request.GET.get('pedido')
    tamanhos = ProdutoInfo.objects.filter(produto=produto_id)
    tamanho = ItensPedido.objects.filter(pedido=pedido_id).filter(produto=produto_id).values_list('tamanho',flat=True)[0]
    return render(request, 'pedidos/ajax/tamanho.html', {'tamanhos': tamanhos,'tamanho':tamanho})

def load_preco(request):
    tamanho = request.GET.get('tamanho')
    preco = ProdutoInfo.objects.get(id=tamanho).preco
    return render(request, 'pedidos/ajax/preco.html', {'preco': preco})

def pedidoDestroy(resquest, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return redirect('/pedidos/')
