import logging
from wsgiref import validate
from xml.dom.minidom import Attr
from django import forms  
from app.models import *  
from django.forms import ModelChoiceField, inlineformset_factory  

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ('nome','desc')

class PizzaForm(forms.ModelForm):
    tamanho = forms.ChoiceField(choices=[("B","B"),("M","M"),("G","G"),("GG","GG")])
    class Meta:
        model = ProdutoInfo
        fields = ('tamanho','preco')

class BebidaForm(forms.ModelForm):
    tamanho = forms.ChoiceField(choices=[("350ml","350ml"),("600ml","600ml"),("1000ml","1000ml"),("1500ml","1500ml"),("2000ml","2000ml")]
    )
    class Meta:
        model = ProdutoInfo
        fields = ('tamanho','preco')


PizzaFormset = inlineformset_factory(Produto, ProdutoInfo, form=PizzaForm,  extra=4, max_num=4, can_delete=True)
BebidaFormset = inlineformset_factory(Produto ,ProdutoInfo, form=BebidaForm,  extra=5, max_num=5, can_delete=True)

class PedidoForm(forms.ModelForm):
    obs = forms.CharField(required=False)
    class Meta:
        model = Pedido
        exclude = ('status','tempo','metodoPag')

class MyModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nome

class ItensPedidoForm(forms.ModelForm):
    produto = MyModelChoiceField(
        widget=forms.Select,
        queryset = Produto.objects.all().filter(cat=1),
        to_field_name='id',
        empty_label="Escolha"
    )

    tamanho = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=ProdutoInfo.objects.none(),
        empty_label="Escolha",
        required=False
    )

    def __init__(self, *args, **kwargs):
        super(ItensPedidoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['readonly'] = True
        if self.data is not None:
            self.fields['tamanho'].queryset = ProdutoInfo.objects.all()
                
    class Meta:
        model = ItensPedido
        fields = '__all__'

PedidoFormset = inlineformset_factory(Pedido, ItensPedido, form=ItensPedidoForm, extra=4, max_num=4, can_delete=True)
