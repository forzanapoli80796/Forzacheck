# Generated by Django 4.2.13 on 2024-12-27 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0020_cleanlinessorderapartment_cold_room_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cleanlinessorderapartment',
            name='floor_image',
            field=models.ImageField(blank=True, null=True, upload_to='floor_image'),
        ),
    ]
