# Generated by Django 3.2.2 on 2021-05-13 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door', '0006_alter_door_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='door',
            name='message',
            field=models.CharField(blank=True, default=None, editable=False, max_length=255),
        ),
    ]
