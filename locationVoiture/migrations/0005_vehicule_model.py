# Generated by Django 4.2 on 2023-05-21 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locationVoiture', '0004_remove_vehicule_model_remove_vehicule_nombreplace_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='model',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]