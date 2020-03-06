# Generated by Django 3.0 on 2020-03-03 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0035_homesettings_date_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesettings',
            name='mini_header',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='homesettings',
            name='video',
            field=models.ImageField(default='wavy.mp4', null=True, upload_to='media/'),
        ),
    ]