# Generated by Django 3.0 on 2020-02-25 10:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('predictions', '0016_auto_20200225_1006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='predictions',
            name='author',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
