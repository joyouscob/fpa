# Generated by Django 3.0 on 2020-01-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0007_auto_20200127_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='posted_under',
            field=models.IntegerField(null=True),
        ),
    ]
