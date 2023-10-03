# Generated by Django 4.2.5 on 2023-10-03 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_alter_vehicle_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='sold_for',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Sold For'),
        ),
    ]
