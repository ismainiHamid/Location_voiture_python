# Generated by Django 4.2 on 2023-05-21 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locationVoiture', '0005_vehicule_model'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='model',
        ),
    ]
