# Generated by Django 3.2.2 on 2021-05-09 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0001_initial'),
        ('door', '0005_alter_door_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Location_Door', to='location.location'),
        ),
    ]
