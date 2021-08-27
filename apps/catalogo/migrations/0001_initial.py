# Generated by Django 3.2.6 on 2021-08-18 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='algas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_cientifico', models.CharField(max_length=200)),
                ('nombre_comun', models.CharField(blank=True, max_length=200, null=True)),
                ('fecha', models.DateTimeField(blank=True, null=True)),
                ('numero_recolecta', models.IntegerField()),
                ('colonia', models.CharField(max_length=200)),
                ('localidad', models.CharField(max_length=200)),
                ('descripcion', models.CharField(max_length=500)),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]