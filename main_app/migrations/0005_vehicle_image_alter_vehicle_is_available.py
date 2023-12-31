# Generated by Django 4.2.5 on 2023-10-02 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_vehicle_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='image',
            field=models.ImageField(default=1, upload_to='dms'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
