# Generated by Django 5.0.6 on 2024-09-03 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ieb', '0008_remove_treinados_atividade_registro_indicador_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treinados',
            name='nome',
        ),
        migrations.RemoveField(
            model_name='treinados',
            name='projeto',
        ),
    ]
