# Generated by Django 3.2.6 on 2021-09-15 20:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0012_alter_polen_especie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algas',
            name='especie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.especie'),
        ),
        migrations.AlterField(
            model_name='frutosemilla',
            name='especie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.especie'),
        ),
        migrations.AlterField(
            model_name='helecho',
            name='especie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.especie'),
        ),
        migrations.AlterField(
            model_name='hongo',
            name='especie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.especie'),
        ),
        migrations.AlterField(
            model_name='planta',
            name='especie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogo.especie'),
        ),
    ]