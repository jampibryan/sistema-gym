# Generated by Django 5.0.6 on 2024-08-30 05:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionD', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TipoGenero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fotoPerfil', models.ImageField(upload_to='imagenes/perfil')),
                ('username', models.CharField(max_length=50)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=50)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comunidad.disciplina')),
                ('genero', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='comunidad.tipogenero')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
