# Generated by Django 3.0 on 2020-02-22 18:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='HydroArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=22)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('data_json', models.TextField()),
                ('image', models.CharField(blank=True, max_length=66, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=32)),
                ('capital', models.CharField(blank=True, max_length=32, null=True)),
                ('lon', models.FloatField(blank=True, null=True)),
                ('lat', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Probable',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('probablename', models.CharField(max_length=30)),
                ('color', models.CharField(blank=True, max_length=11, null=True)),
                ('imgprob', models.CharField(blank=True, db_column='imgProb', max_length=90, null=True)),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('createdby', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Lgas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lga', models.CharField(max_length=32)),
                ('lat', models.FloatField(blank=True, null=True)),
                ('lng', models.FloatField(blank=True, null=True)),
                ('hydro_area', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='predictions.HydroArea')),
                ('lga_state', models.ForeignKey(default=None, on_delete=django.db.models.deletion.PROTECT, to='predictions.State')),
            ],
        ),
    ]