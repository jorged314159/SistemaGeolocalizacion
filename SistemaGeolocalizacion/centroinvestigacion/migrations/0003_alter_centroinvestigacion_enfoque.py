# Generated by Django 4.0.2 on 2022-05-22 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centroinvestigacion', '0002_enfoque_centroinvestigacion_enfoque'),
    ]

    operations = [
        migrations.AlterField(
            model_name='centroinvestigacion',
            name='enfoque',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                    to='centroinvestigacion.enfoque', verbose_name='Enfoque'),
        ),
    ]
