from django import forms  
from app.models import *  
from django.forms import inlineformset_factory  

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome','desc')

class PizzaForm(forms.ModelForm):
    class Meta:
        model = Pizza
        fields = ('tamanho','preco')

class BebidaForm(forms.ModelForm):
    class Meta:
        model = Bebida
        fields = ('tamanho','preco','quant')

PizzaFormset = inlineformset_factory(Produto, Pizza, form=PizzaForm, fields = ('tamanho','preco'), extra=4, max_num=4, can_delete=True)
BebidaFormset = inlineformset_factory(Produto ,Bebida, form=BebidaForm, fields = ('tamanho','preco','quant'), extra=5, max_num=5, can_delete=True)

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        exclude = ('status','tempo','metodoPag')

class ItensPedidoForm(forms.ModelForm):
    nome = forms.ModelChoiceField(
        widget=forms.Select,
        queryset = Produto.objects.all().filter(cat=1).values_list('nome',flat=True),
        empty_label="Selecione o Sabor"
    )

    tamanho = forms.ChoiceField()

    class Meta:
        model = ItensPedido
        fields = '__all__'


PedidoFormset = inlineformset_factory(Pedido,ItensPedido,form=ItensPedidoForm,extra=4,max_num=4,can_delete=True)
