# Generated by Django 4.0.2 on 2022-07-14 01:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centroinvestigacion', '0002_area_alter_centroinvestigacion_subareaenfoque_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centroinvestigacion',
            name='subAreaEnfoque',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='centroinvestigacion.enfoque', verbose_name='Enfoque'),
        ),
        migrations.AlterField(
            model_name='enfoque',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='centroinvestigacion.area', verbose_name='Area'),
        ),
    ]