# Generated by Django 4.0.2 on 2022-05-19 01:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('centroinvestigacion', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfoque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=150, null=True, verbose_name='Descripción')),
            ],
        ),
        migrations.AddField(
            model_name='centroinvestigacion',
            name='enfoque',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.DO_NOTHING, to='centroinvestigacion.enfoque', verbose_name='Enfoque'),
            preserve_default=False,
        ),
    ]