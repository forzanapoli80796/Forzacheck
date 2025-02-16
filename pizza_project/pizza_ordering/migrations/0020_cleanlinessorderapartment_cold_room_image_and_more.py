# Generated by Django 4.2.13 on 2024-12-27 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0019_cleanlinessorderapartment_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='cold_room_image',
            field=models.ImageField(blank=True, null=True, upload_to='cleanliness/cold_room/'),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='floor_image',
            field=models.ImageField(blank=True, null=True, upload_to='cleanliness/floor/'),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='garbage_image',
            field=models.ImageField(blank=True, null=True, upload_to='cleanliness/garbage/'),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='shelf_image',
            field=models.ImageField(blank=True, null=True, upload_to='cleanliness/shelf/'),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='washroom_kitchen_image',
            field=models.ImageField(blank=True, null=True, upload_to='cleanliness/washroom_kitchen/'),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='wc_image',
            field=models.ImageField(blank=True, null=True, upload_to='cleanliness/wc/'),
        ),
    ]
