# Generated by Django 3.0 on 2020-02-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0014_auto_20200201_0905'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='header_img',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='story',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
