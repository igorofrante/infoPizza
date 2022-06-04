from django.db import models

# Create your models here.

class Produto(models.Model):   
    nome = models.CharField(max_length=100,unique=True)  
    desc = models.CharField(max_length=250)
    cat = models.IntegerField()     
    class Meta:  
        db_table = "produto"  

class Pizza(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name='pizza')
    tamanho = models.CharField(max_length=2,choices=[("B","B"),("M","M"),("G","G"),("GG","GG")])
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "pizza"
        unique_together = ['tamanho', 'produto']

class Bebida(models.Model):
    produto = models.ForeignKey(Produto,on_delete=models.CASCADE,related_name='bebida')
    tamanho = models.CharField(max_length=6,choices=[("350ml","350ml"),("600ml","600ml"),("1000ml","1000ml"),("1500ml","1500ml"),("2000ml","2000ml")])
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    quant = models.IntegerField()
    class Meta:
        db_table = "bebida"
        unique_together = ['tamanho', 'produto']

class Pedido(models.Model):
    status = models.CharField(default="Inicio",max_length=100)
    tempo = models.DateTimeField(auto_now_add=True)
    metodoPag = models.CharField(null=True,max_length=50)
    obs = models.CharField(max_length=500)
    class Meta:
        db_table = "pedido"

class ItensPedido(models.Model):
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tamanho = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=4,decimal_places=2)
    class Meta:
        db_table = "itensPedido"

class Mesa(models.Model):
    status = models.BooleanField()
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    class Meta:
        db_table = "mesa"
