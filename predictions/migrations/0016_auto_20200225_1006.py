# Generated by Django 3.0 on 2020-02-25 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0015_auto_20200225_0855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='actual_occurence',
            field=models.TextField(default=None, null=True),
        ),
    ]