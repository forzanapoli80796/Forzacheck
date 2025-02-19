# Generated by Django 4.2.13 on 2024-10-07 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0002_rename_measures_cleanlinessorderkitchen_bottom_sink_comment_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cleanlinessorderapartment',
            old_name='measures',
            new_name='cold_room_comment',
        ),
        migrations.RenameField(
            model_name='cleanlinessorderstorage',
            old_name='measures',
            new_name='floor_comment',
        ),
        migrations.RenameField(
            model_name='cleanlinessorderterminal',
            old_name='measures',
            new_name='counter_comment',
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='floor_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='garbage_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='shelf_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='washroom_kitchen_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderapartment',
            name='wc_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderstorage',
            name='garbage_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderstorage',
            name='inventory_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderstorage',
            name='tidiness_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderterminal',
            name='floor_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderterminal',
            name='lamps_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderterminal',
            name='refrigerator_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderterminal',
            name='tables_chairs_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderterminal',
            name='tiles_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderterminal',
            name='windows_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
