# Generated by Django 5.1.3 on 2025-02-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0038_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Fácil', 'Fácil'), ('Médio', 'Médio'), ('Difícil', 'Difícil')], default='Fácil', max_length=30),
        ),
    ]
