from wsgiref import validate
from xml.dom.minidom import Attr
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
    obs = forms.CharField(required=False)
    class Meta:
        model = Pedido
        exclude = ('status','tempo','metodoPag')

class ItensPedidoForm(forms.ModelForm):
    nome = forms.ModelChoiceField(
        widget=forms.Select,
        queryset = Produto.objects.all().filter(cat=1).values_list('nome',flat=True),
        empty_label="Selecione o Sabor",
        required=False
    )

    tamanho = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        super(ItensPedidoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].widget.attrs['readonly'] = True
        self.fields['tamanho'].queryset = Pizza.objects.none()

        if 'nome' in self.data:
            try:
                produto_id = self.data.get('produto')
                produto_id = Produto.objects.get(nome=produto_id).id
                self.fields['tamanho'].queryset = Pizza.objects.filter(produto=produto_id)
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset


    class Meta:
        model = ItensPedido
        fields = '__all__'

PedidoFormset = inlineformset_factory(Pedido, ItensPedido, form=ItensPedidoForm, extra=4, max_num=4, can_delete=True)
