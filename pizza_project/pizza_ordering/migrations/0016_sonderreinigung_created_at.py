# Generated by Django 4.2.13 on 2024-12-13 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza_ordering', '0015_ebikecondition_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='sonderreinigung',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
