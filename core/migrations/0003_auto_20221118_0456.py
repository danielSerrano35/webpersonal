# Generated by Django 3.2 on 2022-11-18 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20221118_0431'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Autos',
        ),
        migrations.DeleteModel(
            name='Categoria',
        ),
    ]
