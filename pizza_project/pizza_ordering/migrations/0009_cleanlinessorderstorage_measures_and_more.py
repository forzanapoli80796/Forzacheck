# Generated by Django 4.2.13 on 2024-10-20 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0008_cleanlinessorderkitchen_measures'),
    ]

    operations = [
        migrations.AddField(
            model_name='cleanlinessorderstorage',
            name='measures',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cleanlinessorderterminal',
            name='measures',
            field=models.TextField(blank=True, null=True),
        ),
    ]
