# Generated by Django 3.2.7 on 2021-09-15 18:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankcontroller', '0010_moneytransfer_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.DecimalValidator(decimal_places=2, max_digits=10)], verbose_name='Цена услуги'),
        ),
    ]
