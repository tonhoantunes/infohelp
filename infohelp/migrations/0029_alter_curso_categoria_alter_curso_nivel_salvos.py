# Generated by Django 5.1.3 on 2025-02-13 19:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infohelp', '0028_alter_curso_categoria_alter_curso_nivel'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='curso',
            name='categoria',
            field=models.CharField(choices=[('Design', 'Design'), ('Texto', 'Texto'), ('Planilha', 'Planilha'), ('Apresentação', 'Apresentação')], max_length=100),
        ),
        migrations.AlterField(
            model_name='curso',
            name='nivel',
            field=models.CharField(choices=[('Médio', 'Médio'), ('Fácil', 'Fácil'), ('Difícil', 'Difícil')], default='Fácil', max_length=30),
        ),
        migrations.CreateModel(
            name='Salvos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cursos', models.ManyToManyField(related_name='salvos', to='infohelp.curso')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salvos', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
