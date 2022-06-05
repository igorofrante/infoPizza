from django.db import models

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

class Pedido(models.Model):
    status = models.CharField(default="Inicio",max_length=100)
    tempo = models.DateTimeField(auto_now_add=True)
    metodoPag = models.CharField(null=True,max_length=50)
    obs = models.CharField(max_length=500, null=True)
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
    status = models.BooleanField()
    pedido = models.ForeignKey(Pedido,on_delete=models.CASCADE)
    class Meta:
        db_table = "mesa"
