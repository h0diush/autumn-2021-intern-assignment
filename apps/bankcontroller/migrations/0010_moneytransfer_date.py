# Generated by Django 3.2.7 on 2021-09-13 21:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bankcontroller', '0009_delete_infolsit'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneytransfer',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
