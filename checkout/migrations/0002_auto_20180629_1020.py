# Generated by Django 2.0.6 on 2018-06-29 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='status_order',
            field=models.CharField(choices=[('A', 'active'), ('I', 'INACTIVE')], default='A', max_length=10, verbose_name='Status do Pedido'),
        ),
    ]
