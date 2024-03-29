# Generated by Django 4.2.5 on 2024-03-25 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0011_alojamiento_propietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alojamiento',
            name='imagen',
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(upload_to='alojamientos')),
                ('alojamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='aplicacion.alojamiento')),
            ],
        ),
        migrations.CreateModel(
            name='Disponibilidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateField()),
                ('disponibilidad', models.BooleanField(default=True)),
                ('alojamiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacion.alojamiento')),
            ],
        ),
    ]