# Generated by Django 4.0.2 on 2022-08-04 23:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=150, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Enfoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subarea', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(max_length=150, verbose_name='Descripción')),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='centroinvestigacion.area', verbose_name='Area')),
            ],
        ),
        migrations.CreateModel(
            name='CentroInvestigacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, unique=True)),
                ('calle', models.CharField(max_length=150, verbose_name='Calle')),
                ('colonia', models.CharField(max_length=150, verbose_name='Colonia')),
                ('numExterior', models.CharField(max_length=5, verbose_name='Numero Exterior')),
                ('cp', models.CharField(max_length=5, verbose_name='Codigo Postal')),
                ('estado', models.CharField(max_length=150, verbose_name='Estado')),
                ('municipio', models.CharField(max_length=150, verbose_name='Municipio')),
                ('latitud', models.CharField(max_length=20, unique=True)),
                ('longitud', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=10, unique=True, verbose_name='Telefono')),
                ('sitioWeb', models.CharField(blank=True, max_length=100, unique=True)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='foto/')),
                ('areaEnfoque', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='centroinvestigacion.area', verbose_name='Area')),
                ('subAreaEnfoque', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='centroinvestigacion.enfoque', verbose_name='Subarea')),
            ],
        ),
    ]
