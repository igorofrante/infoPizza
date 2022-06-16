# Generated by Django 4.0.4 on 2022-06-15 22:33

from django.db import migrations, models
import django.db.models.deletion
import localflavor.br.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200)),
                ('sobrenome', models.CharField(max_length=200)),
                ('cpf', localflavor.br.models.BRCPFField(max_length=14, unique=True)),
                ('telefone', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('cep', localflavor.br.models.BRPostalCodeField(max_length=9)),
                ('logradouro', models.CharField(max_length=200)),
                ('numero', models.PositiveIntegerField()),
                ('complemento', models.CharField(max_length=200, null=True)),
                ('bairro', models.CharField(max_length=200)),
                ('cidade', models.CharField(max_length=200)),
                ('referencia', models.CharField(max_length=200)),
                ('cadastro', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'cliente',
            },
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, unique=True)),
                ('desc', models.CharField(max_length=250)),
                ('cat', models.IntegerField()),
            ],
            options={
                'db_table': 'produto',
            },
        ),
        migrations.CreateModel(
            name='ProdutoInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tamanho', models.CharField(max_length=6)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bebida', to='app.produto')),
            ],
            options={
                'db_table': 'produtoInfo',
                'unique_together': {('tamanho', 'produto')},
            },
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat', models.IntegerField()),
                ('status', models.CharField(default='Inicio', max_length=100)),
                ('tempo', models.DateTimeField(auto_now_add=True)),
                ('metodoPag', models.CharField(max_length=50, null=True)),
                ('obs', models.CharField(max_length=500, null=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.cliente')),
            ],
            options={
                'db_table': 'pedido',
            },
        ),
        migrations.CreateModel(
            name='Mesa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('pedido', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
            ],
            options={
                'db_table': 'mesa',
            },
        ),
        migrations.CreateModel(
            name='ItensPedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=4)),
                ('pedido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.pedido')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produto')),
                ('tamanho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.produtoinfo')),
            ],
            options={
                'db_table': 'itensPedido',
            },
        ),
    ]
