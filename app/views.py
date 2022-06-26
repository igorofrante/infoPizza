from dataclasses import fields
from datetime import datetime,timedelta,time
from re import M
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.db.models import Sum
from app.forms import * 
from app.models import *

import logging

# logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
# logging.debug(form)

# Create your views here.

# def index(request):
#     ##############################################################################
#     if datetime.now().time() < time(23,59): 
#         startdate =  datetime.now()
#         startdate = startdate.replace(hour=18,minute=0,second=0)
#         enddate = startdate + timedelta(days=1)
#         enddate = enddate.replace(hour=5,minute=0,second=0)
#     else:
#         startdate =  datetime.now() - timedelta(days=1)
#         startdate = startdate.replace(hour=18,minute=0,second=0)
#         enddate = datetime.now()
#         enddate= enddate.replace(hour=5,minute=0,second=0) 
#     ############################################################################
#     pedidoshoje = Pedido.objects.filter(tempo__range=(startdate,enddate)).count()
#     faturadohoje= Pedido.objects.filter(tempo__range=(startdate,enddate)).filter(status="Finalizado").aggregate(Sum('total'))['total__sum']
#     if faturadohoje == None:
#         faturadohoje="00,00"
#     else:
#         faturadohoje = str(faturadohoje).replace(".",",")
#     clientesnovoshoje = Cliente.objects.filter(cadastro__range=(startdate,enddate)).count()
#     cincoClientes = Cliente.objects.all().order_by('-id')[:5]
#     cincoPedidos = Pedido.objects.all().order_by('-id')[:5]
#     return render(request, 'index.html', {'pedidoshoje':pedidoshoje,'faturadohoje':faturadohoje,'clientesnovoshoje':clientesnovoshoje, 'cincoClientes':cincoClientes, 'cincoPedidos':cincoPedidos})

def index(request):
    pedidoshoje = Pedido.objects.all().count()
    faturadohoje= Pedido.objects.filter(status="Finalizado").aggregate(Sum('total'))['total__sum']
    if faturadohoje == None:
        faturadohoje="00,00"
    else:
        faturadohoje = str(faturadohoje).replace(".",",")
    clientesnovoshoje = Cliente.objects.count()
    cincoClientes = Cliente.objects.all().order_by('-id')[:5]
    cincoPedidos = Pedido.objects.all().order_by('-id')[:5]
    return render(request, 'index.html', {'pedidoshoje':pedidoshoje,'faturadohoje':faturadohoje,'clientesnovoshoje':clientesnovoshoje, 'cincoClientes':cincoClientes, 'cincoPedidos':cincoPedidos})


############ CARDAPIO ############
############ PIZZA    ############
def cardapioPizzaIndex(request):
    pizzas = Produto.objects.filter(cat__iexact=1).order_by('nome') 
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
    return render(request,'cardapio/pizza/form.html', {'form':form,'form2':form2,'titulo':'Cadastrar Pizza'})  

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
            pass
    else:
        form = ProdutoForm(instance=pizza, prefix='form')
        form2 = PizzaFormset(instance=pizza, prefix='form2')
    return render(request, 'cardapio/pizza/form.html', {'form':form,'form2':form2,'pizza':pizza,'titulo':'Editar Pizza'})  

def cardapioPizzaDestroy(request, id):  
    pizza = Produto.objects.get(id=id)  
    pizza.delete()  
    return redirect("/cardapio/pizza")

############ CARDAPIO ############
############ BEBIDA   ############
def cardapioBebidaIndex(request) :
    bebidas = Produto.objects.filter(cat__iexact=2).order_by('nome')
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
    return render(request,'cardapio/bebida/form.html', {'form':form, 'form2':form2,'titulo':'Cadastrar Bebida'})  

def cardapioBebidaUpdate(request, id):  
    bebida = Produto.objects.get(id=id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=bebida, prefix='form')
        form2 = BebidaFormset(request.POST, instance=bebida, prefix='form2')
        if form.is_valid() and form2.is_valid():  
            form.save()
            form2.save()
            return redirect('/cardapio/bebida')  
    else:
        form = ProdutoForm(instance=bebida, prefix='form')
        form2 = BebidaFormset(instance=bebida, prefix='form2')
    return render(request, 'cardapio/bebida/form.html', {'form':form,'form2':form2,'bebida':bebida,'titulo':'Editar Bebida'})  

def cardapioBebidaDestroy(request, id):  
    bebida = Produto.objects.get(id=id)  
    bebida.delete()  
    return redirect("/cardapio/bebida")

########### CLIENTE ############
def clienteIndex(request):
    clientes = Cliente.objects.all().order_by('nome')
    return render(request, 'cliente/index.html', {'clientes':clientes})

def clienteView(request,id):
     cliente = Cliente.objects.get(id=id)
     pedidos = Pedido.objects.filter(cliente=id).order_by('-tempo')
     return render(request, 'cliente/view.html', {'cliente':cliente,'pedidos':pedidos})

def clienteInsert(request):
    if request.method == "POST":
        form = clienteForm(request.POST)
        if form.is_valid():  
            form.save()
            return redirect('/cliente/')  
    else:  
        form = clienteForm()
    return render(request,'cliente/form.html', {'form':form,'titulo':'Cadastrar Cliente'})  

def clienteUpdate(request, id):
    cliente = Cliente.objects.get(id=id)
    if request.method == "POST":
        form = clienteForm(request.POST, instance=cliente)
        if form.is_valid():  
            form.save()
            return redirect('/cliente/')  
    else:  
        form = clienteForm(instance=cliente)
    return render(request,'cliente/form.html', {'form':form,'titulo':'Editar Cliente'})  

def clienteDestroy(request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('/cliente/')

########### PEDIDOS ############
def pedidosIndex(request) :
    pedidos = Pedido.objects.all().order_by('-tempo')
    return render(request,"pedido/index.html",{'pedidos':pedidos,'titulo':'Todos os pedidos'}) 
def pedidosDeliveryIndex(request) :
    pedidos = Pedido.objects.filter(cat=1).order_by('-tempo')
    return render(request,"pedido/index.html",{'pedidos':pedidos,'titulo':'Pedidos - Delivery'}) 
def pedidosMesaIndex(request) :
    pedidos = Pedido.objects.filter(cat=2).order_by('-tempo')
    return render(request,"pedido/index.html",{'pedidos':pedidos,'titulo':'Pedidos - Mesa'})     



def pedidosDeliveryInsert(request) :
    novoPedido = Pedido(cat=1)
    if request.method == "POST":
        form = PedidoForm(request.POST,instance=novoPedido, prefix='form')
        formp = PedidoPizzaFormset(request.POST, instance=novoPedido, prefix='formp')
        formb = PedidoBebidaFormset(request.POST, instance=novoPedido, prefix='formb')

        if form.is_valid() and formp.is_valid() and formb.is_valid():  
            try:  
                form.save()
                formb.save()
                formp.save()
                return redirect('/pedido/delivery')  
            except:  
                pass  

    else:  
        form = PedidoForm(instance=novoPedido,prefix='form')
        formp = PedidoPizzaFormset(instance=novoPedido,prefix='formp')
        formb = PedidoBebidaFormset(instance=novoPedido,prefix='formb')
    return render(request,'pedido/form.html', {'form':form, 'formp':formp, 'formb':formb, 'titulo':'Anotar Pedido - Delivery'})  

def pedidosMesaInsert(request) :
    novoPedido = Pedido(cat=2)
    if request.method == "POST":
        form = PedidoForm(request.POST,instance=novoPedido, prefix='form')
        formp = PedidoPizzaFormset(request.POST, instance=novoPedido, prefix='formp')
        formb = PedidoBebidaFormset(request.POST, instance=novoPedido, prefix='formb')
        formm = mesaForm(request.POST, prefix='formm')
        if form.is_valid() and formp.is_valid() and formb.is_valid() and formm.is_valid():  
            try:  
                form.save()
                formb.save()
                formp.save()
                mesa = Mesa.objects.get(id=request.POST['formm-id'])
                mesa.pedido = form.instance.id    
                mesa.save()        
                return redirect('/pedido/mesa')  
            except:  
                pass  
    else:  
        form = PedidoForm(instance=novoPedido,prefix='form')
        formp = PedidoPizzaFormset(instance=novoPedido,prefix='formp')
        formb = PedidoBebidaFormset(instance=novoPedido,prefix='formb')
        formm = mesaForm(instance=novoPedido,prefix='formm')
    return render(request,'pedido/form.html', {'form':form, 'formp':formp, 'formb':formb, 'formm':formm, 'titulo':'Anotar Pedido - Mesa'})  


def pedidosUpdate(request, id):
    pedido = Pedido.objects.get(id=id)
    if Pedido.objects.get(id=id).cliente != None:
        cliente_id = Pedido.objects.get(id=id).cliente.id
    else:
        cliente_id = None
    titulo = ""
    if(pedido.cat == 1):
        titulo = 'Editar Pedido - Delivery'
    else:
        titulo = 'Editar Pedido - Mesa'
    if request.method == "POST":
        form = PedidoForm2(request.POST,instance=pedido, prefix='form')
        formp = PedidoPizzaFormset(request.POST,instance=pedido, prefix='formp')
        formb = PedidoBebidaFormset(request.POST,instance=pedido, prefix='formb')
        if form.is_valid() and formb.is_valid() and formp.is_valid():  
            try:  
                form.save()
                formb.save()
                formp.save()
                return redirect('/pedido')  
            except:  
                pass  
    else:  
        form = PedidoForm2(instance=pedido,prefix='form')
        formp = PedidoPizzaFormset(instance=pedido,queryset=ItensPedido.objects.filter(pedido=id).filter(produto__cat=1),prefix='formp')
        formb = PedidoBebidaFormset(instance=pedido,queryset=ItensPedido.objects.filter(pedido=id).filter(produto__cat=2),prefix='formb')
        if cliente_id != None:
            cliente = Cliente.objects.get(id=cliente_id)
            clienteinfo = cliente.nome+" "+cliente.sobrenome+" ("+cliente.cpf+")" 
        else:
            clienteinfo = "Não informado"
    return render(request,'pedido/form.html',{'form':form, 'formp':formp, 'formb':formb,'pedido':pedido,'clienteinfo':clienteinfo,'titulo':titulo})
        
def load_tamanhos(request):
    produto_id = request.GET.get('produto')
    tamanhos = ProdutoInfo.objects.filter(produto=produto_id)
    return render(request, 'pedido/ajax/tamanhos.html', {'tamanhos': tamanhos})

def load_tamanhos2(request):
    produto_id = request.GET.get('produto')
    tamanhos = ProdutoInfo.objects.filter(produto=produto_id)
    return render(request, 'pedido/ajax/tamanhos2.html', {'tamanhos': tamanhos})

def load_tamanho(request):
    itensPedido_id = request.GET.get('idx')
    tamanho = ItensPedido.objects.get(id=itensPedido_id).tamanho.id
    return render(request, 'pedido/ajax/tamanho.html', {'tamanho':tamanho})

def load_preco(request):
    tamanho = request.GET.get('tamanho')
    preco = ProdutoInfo.objects.get(id=tamanho).preco
    return render(request, 'pedido/ajax/preco.html', {'preco': preco})

def pedidoWaiter(request, id):
    pedido = Pedido.objects.get(id=id)
    if pedido.status == "Pedido Pronto":
        pedido.status = "Servido"
        pedido.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def pedidoDelivery(request, id):
    pedido = Pedido.objects.get(id=id)
    if pedido.status == "Pedido Pronto":
        pedido.status = "Saiu para entrega"
        pedido.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def pedidoCancel(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.status = "Cancelado"
    pedido.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def pedidoDestroy(request, id):
    pedido = Pedido.objects.get(id=id)
    pedido.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


########### MESA ############
def mesaIndex(request):
    mesas = Mesa.objects.all()
    return render(request, 'mesa/index.html', {'mesas': mesas})

def mesaInsert(request):
    mesa = Mesa()
    mesa.save()
    return redirect('/mesa/')

def mesaClean(request,id):
    mesa = Mesa.objects.get(id=id)
    mesa.pedido = None
    mesa.save()
    return redirect('/mesa/')

def mesaDestroy(request,id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect('/mesa/')

########### COZINHA ############

def cozinhaIndex(request):
    pedidos = Pedido.objects.filter(status__in=['Anotado', 'Preparando','Pedido Pronto'])
    return render(request, 'cozinha/index.html', {'pedidos': pedidos})

def cozinhaView(request, id):
    pedido = Pedido.objects.get(id=id)
    itensPizza = ItensPedido.objects.filter(pedido=pedido.id).filter(produto__cat=1)
    itensBebida = ItensPedido.objects.filter(pedido=pedido.id).filter(produto__cat=2)

    dic = {'pedido':pedido, 'pizzas':itensPizza, 'bebidas':itensBebida }

    return render(request,'cozinha/view.html', dic)

def cozinhaUpdate(request, id, status):
    pedido = Pedido.objects.get(id=id)
    if status == 1:
        pedido.status = 'Preparando'
    elif status == 2:
        pedido.status = 'Pedido Pronto'
    else:
        pedido.status = 'Cancelado'
    
    pedido.save()

    return redirect('/cozinha/')

########### CAIXA ############


def caixaIndex(request):
    pedidos = Pedido.objects.filter(status__in=['Saiu para entrega', 'Servido'])
    return render(request, 'caixa/index.html', {'pedidos': pedidos})


def caixaView(request, id):
    pedido = Pedido.objects.get(id=id)
    itensPizza = ItensPedido.objects.filter(pedido=pedido.id).filter(produto__cat=1)
    itensBebida = ItensPedido.objects.filter(pedido=pedido.id).filter(produto__cat=2)

    if request.method == "POST":
        form = caixaForm(request.POST,instance=pedido, prefix='form')
        if form.is_valid() :   
            form.save()
            pedido.status = 'Finalizado'
            pedido.save()
            if pedido.cat == 2:
                mesa = Mesa.objects.get(pedido=pedido.id)
                mesa.pedido = None
                mesa.save()
            return redirect('/caixa')  
    else:  
        form = caixaForm(instance=pedido, prefix='form')

    dic = {'form':form, 'pedido':pedido, 'pizzas':itensPizza, 'bebidas':itensBebida }

    return render(request,'caixa/view.html', dic)