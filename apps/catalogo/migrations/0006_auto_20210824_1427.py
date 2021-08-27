# Generated by Django 3.2.6 on 2021-08-24 19:27

import apps.catalogo.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0005_alter_algas_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algas',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='algas',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='frutosemilla',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='frutosemilla',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='helecho',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='helecho',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='hongo',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='hongo',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='planta',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='planta',
            name='genero',
        ),
        migrations.RemoveField(
            model_name='polen',
            name='especie',
        ),
        migrations.RemoveField(
            model_name='polen',
            name='genero',
        ),
        migrations.AddField(
            model_name='especie',
            name='familia',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.familia'),
        ),
        migrations.AlterField(
            model_name='frutosemilla',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=apps.catalogo.models.FrutoSemilla.get_upload_path_imagen),
        ),
        migrations.AlterField(
            model_name='helecho',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=apps.catalogo.models.Helecho.get_upload_path_imagen),
        ),
        migrations.AlterField(
            model_name='hongo',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=apps.catalogo.models.Hongo.get_upload_path_imagen),
        ),
        migrations.AlterField(
            model_name='planta',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=apps.catalogo.models.Planta.get_upload_path_imagen),
        ),
        migrations.AlterField(
            model_name='polen',
            name='imagen',
            field=models.FileField(blank=True, null=True, upload_to=apps.catalogo.models.Polen.get_upload_path_imagen),
        ),
        migrations.DeleteModel(
            name='genero',
        ),
    ]