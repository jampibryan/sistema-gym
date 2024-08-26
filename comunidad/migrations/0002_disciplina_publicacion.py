# Generated by Django 5.0.6 on 2024-08-26 01:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comunidad', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcionDisciplina', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaPublicacion', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(blank=True, upload_to='imagenes/')),
                ('mensaje', models.TextField(blank=True)),
                ('disciplina', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comunidad.disciplina')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='comunidad.usuario')),
            ],
        ),
    ]
