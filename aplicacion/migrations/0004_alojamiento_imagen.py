# Generated by Django 5.0.2 on 2024-03-09 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_alojamiento_ciudad_alojamiento_direccion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamiento',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='alojamientos/'),
        ),
    ]