# Generated by Django 4.2 on 2023-05-21 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationVoiture', '0006_remove_vehicule_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='prix',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]