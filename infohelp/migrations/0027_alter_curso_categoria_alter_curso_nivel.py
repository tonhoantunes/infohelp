# Generated by Django 5.1.3 on 2025-02-12 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0026_alter_curso_categoria_alter_curso_nivel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='categoria',
            field=models.CharField(choices=[('Planilha', 'Planilha'), ('Texto', 'Texto'), ('Design', 'Design'), ('Apresentação', 'Apresentação')], max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Fácil', 'Fácil'), ('Difícil', 'Difícil'), ('Médio', 'Médio')], default='Fácil', max_length=30),
        ),
    ]
