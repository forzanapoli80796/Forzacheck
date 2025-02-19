# Generated by Django 4.2.13 on 2024-10-07 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cleanlinessorderkitchen',
            old_name='measures',
            new_name='bottom_sink_comment',
        ),
        migrations.AddField(
            model_name='cleanlinessorderkitchen',
            name='extractor_hood_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderkitchen',
            name='kav_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderkitchen',
            name='refrigerator_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderkitchen',
            name='refrigerators_back_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderkitchen',
            name='tables_downstairs_comment',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderkitchen',
            name='tiles_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
