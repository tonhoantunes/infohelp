# Generated by Django 5.1.3 on 2025-02-03 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0017_remove_aula_curso_aula_curso'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='link',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='aula',
            name='descricao',
            field=models.TextField(blank=True, max_length=2000),
        ),
    ]
