# Generated by Django 3.2.2 on 2021-05-13 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('door', '0009_remove_door_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='door_name',
            field=models.CharField(max_length=50, null=True, unique=True),
        ),
    ]
