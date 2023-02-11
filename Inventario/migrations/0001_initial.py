# Generated by Django 3.2 on 2022-11-18 09:59

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(default='SOME STRING', max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(default='SOME STRING', editable=False, populate_from='nombre')),
                ('activo', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Autos',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('modelo', models.CharField(default='SOME STRING', max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(default='SOME STRING', editable=False, populate_from='nombre')),
                ('imagen', models.CharField(default='SOME STRING', max_length=250)),
                ('marca', models.CharField(default='SOME STRING', max_length=20)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('renta', models.DecimalField(decimal_places=2, default=0.0, max_digits=15)),
                ('activo', models.BooleanField(default=True)),
                ('categoria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Inventario.categoria')),
            ],
        ),
    ]