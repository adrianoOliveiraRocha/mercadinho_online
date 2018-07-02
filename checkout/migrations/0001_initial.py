# Generated by Django 2.0.6 on 2018-06-29 12:32

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0003_remove_product_expiration_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today, editable=False)),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor R$')),
                ('status', models.CharField(choices=[('1', 'Completo'), ('2', 'Aprovado'), ('3', 'Em Análise'), ('4', 'Devolvido'), ('5', 'Cancelado')], default='EA', max_length=2, verbose_name='Status do Pedido')),
                ('delivery_address_is_the_same', models.BooleanField(default=True, verbose_name='Entregar no endereço cadastrado')),
                ('logradouro', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Rua/Avenida')),
                ('numero', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Número')),
                ('cep', models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='CEP')),
                ('complemento', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Complamento')),
                ('bairro', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Bairro')),
                ('cidade', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Cidade')),
                ('estado', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Estado')),
                ('transaction_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='ID da transação')),
                ('status_pg', models.CharField(choices=[('1', 'Completo'), ('2', 'Aprovado'), ('3', 'Em Análise'), ('4', 'Devolvido'), ('5', 'Cancelado')], default=None, max_length=10, verbose_name='Status PagSeguro')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveSmallIntegerField(default=1, editable=False, verbose_name='Quantidade')),
                ('value', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Valor R$')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='checkout.Order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.Product')),
            ],
            options={
                'verbose_name': 'Ítem de Pedido',
                'verbose_name_plural': 'Ítens de Pedido',
                'ordering': ['order'],
            },
        ),
    ]