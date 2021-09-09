# Generated by Django 3.2.7 on 2021-09-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcontroller', '0003_alter_moneycard_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='currency',
            field=models.CharField(choices=[('USD', 'USD'), ('RUB', 'RUB'), ('EUR', 'EUR')], default='RUB', max_length=6, verbose_name='Валюта'),
        ),
    ]
