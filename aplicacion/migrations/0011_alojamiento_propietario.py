# Generated by Django 4.2.5 on 2024-03-22 14:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0010_remove_avatar_avatar_remove_usuario_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alojamiento',
            name='propietario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]