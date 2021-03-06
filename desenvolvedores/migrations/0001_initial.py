# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-22 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Desenvolvedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('equipe', models.CharField(max_length=50)),
                ('presente', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=3)),
                ('quentinha_dia1', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=3)),
                ('carne_dia1', models.CharField(choices=[('Nenhuma', 'Nenhuma'), ('Frango Assado', 'Frango Assado'), ('Linguiça', 'Linguiça'), ('Carne Assada na Brasa', 'Carne Assada na Brasa'), ('Galinha', 'Galinha')], max_length=30)),
                ('quentinha_dia2', models.CharField(choices=[('Não', 'Não'), ('Sim', 'Sim')], max_length=3)),
                ('carne_dia2', models.CharField(choices=[('Nenhuma', 'Nenhuma'), ('Frango Assado', 'Frango Assado'), ('Linguiça', 'Linguiça'), ('Carne Assada na Brasa', 'Carne Assada na Brasa'), ('Galinha', 'Galinha')], max_length=30)),
            ],
        ),
    ]
