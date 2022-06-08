from asyncio.windows_events import NULL
import logging
from pickle import EMPTY_DICT
from queue import Empty
from wsgiref import validate
from xml.dom.minidom import Attr
from django import forms  
from app.models import *  
from django.forms import ModelChoiceField, inlineformset_factory  
from django.db.models.fields import BLANK_CHOICE_DASH

class ProdutoForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea)
    class Meta:
        model = Produto
        fields = ('nome','desc')

class PizzaForm(forms.ModelForm):
    tamanho = forms.ChoiceField(choices= BLANK_CHOICE_DASH + [("B","B"),("M","M"),("G","G"),("GG","GG")])
    class Meta:
        model = ProdutoInfo
        fields = ('tamanho','preco')

class BebidaForm(forms.ModelForm):
    tamanho = forms.ChoiceField(choices= BLANK_CHOICE_DASH + [("350ml","350ml"),("600ml","600ml"),("1000ml","1000ml"),("1500ml","1500ml"),("2000ml","2000ml")]
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
    )

    def __init__(self, *args, **kwargs):
        super(ItensPedidoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['readonly'] = True
        if self.data != {}:
            self.fields['tamanho'].queryset = ProdutoInfo.objects.all()
        logging.basicConfig(filename='mylog.log', level=logging.DEBUG)
        logging.debug(self.data)
    
                
    class Meta:
        model = ItensPedido
        fields = '__all__'

class ItensPedidoForm2(forms.ModelForm):
    produto = MyModelChoiceField(
        widget=forms.Select,
        queryset = Produto.objects.all().filter(cat=2),
        to_field_name='id',
        empty_label="Escolha"
    )

    tamanho = forms.ModelChoiceField(
        widget=forms.Select,
        queryset=ProdutoInfo.objects.none(),
        empty_label="Escolha",
    )

    def __init__(self, *args, **kwargs):
        super(ItensPedidoForm2, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['readonly'] = True
        if self.data != {}:
            self.fields['tamanho'].queryset = ProdutoInfo.objects.all()
                
    class Meta:
        model = ItensPedido
        fields = '__all__'


PedidoPizzaFormset = inlineformset_factory(Pedido, ItensPedido, form=ItensPedidoForm, extra=4, max_num=4, can_delete=True)
PedidoBebidaFormset = inlineformset_factory(Pedido, ItensPedido, form=ItensPedidoForm2, extra=4, max_num=4, can_delete=True)
