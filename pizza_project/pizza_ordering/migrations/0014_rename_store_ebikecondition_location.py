# Generated by Django 4.2.13 on 2024-12-13 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0013_bestbeforedatecheck_date_terminalinventory_pflaster_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ebikecondition',
            old_name='store',
            new_name='location',
        ),
    ]
