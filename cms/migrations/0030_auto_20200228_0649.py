# Generated by Django 3.0 on 2020-02-28 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0029_auto_20200228_0649'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='page',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='cms.Page'),
        ),
    ]
