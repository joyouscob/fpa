# Generated by Django 3.0 on 2020-01-27 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0006_page_menu_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='menu_title',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
