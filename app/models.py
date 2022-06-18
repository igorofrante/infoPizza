from django.db import models
from localflavor.br.models import BRCPFField, BRPostalCodeField
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

class Produto(models.Model):   
    nome = models.CharField(max_length=100,unique=True)  
    desc = models.CharField(max_length=250)
    cat = models.IntegerField()     
    class Meta:  
        db_table = "produto"  

class ProdutoInfo(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name='bebida')
    tamanho = models.CharField(max_length=6)
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "produtoInfo"
        unique_together = ['tamanho', 'produto']

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    cpf = BRCPFField(unique=True)
    dtnasc = models.DateField()  
    telefone = PhoneNumberField()
    cep = BRPostalCodeField()
    logradouro = models.CharField(max_length=200)
    numero = models.PositiveIntegerField()
    complemento = models.CharField(max_length=200, null=True)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    cadastro = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = "cliente"

class Pedido(models.Model):
    cat = models.IntegerField()
    status = models.CharField(default="Anotado",max_length=100)
    tempo = models.DateTimeField(auto_now_add=True)
    metodoPag = models.CharField(null=True,max_length=50)
    obs = models.CharField(max_length=500, null=True)
    cliente = models.ForeignKey(Cliente,null=True,on_delete=models.SET_NULL)
    class Meta:
        db_table = "pedido"

class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE)
    tamanho = models.ForeignKey(ProdutoInfo,on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "itensPedido"

class Mesa(models.Model):
    pedido = models.IntegerField(null=True)
    class Meta:
        db_table = "mesa"


