# Generated by Django 3.0 on 2020-02-24 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0024_auto_20200224_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stories',
            name='title',
            field=models.CharField(default='Story', max_length=100, null=True),
        ),
    ]
