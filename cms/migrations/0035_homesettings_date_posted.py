# Generated by Django 3.0 on 2020-03-03 16:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0034_homesettings_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesettings',
            name='date_posted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
