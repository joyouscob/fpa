# Generated by Django 3.0 on 2020-02-22 19:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('predictions', '0005_auto_20200222_1942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lgas',
            old_name='lga',
            new_name='name',
        ),
    ]
