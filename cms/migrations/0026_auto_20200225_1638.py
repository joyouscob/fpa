# Generated by Django 3.0 on 2020-02-25 16:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0025_auto_20200224_1454'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='menuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cms.Menu'),
        ),
    ]
