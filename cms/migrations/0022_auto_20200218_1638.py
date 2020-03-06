# Generated by Django 3.0 on 2020-02-18 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0021_auto_20200201_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='email',
            field=models.EmailField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='story',
            name='phone',
            field=models.CharField(default=None, max_length=11, null=True),
        ),
    ]