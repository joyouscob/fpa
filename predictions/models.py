from django.db import models

# Create your models here.
from django.db import models
# import the timezone module for date and time
from django.utils import timezone
#import the user model from django
from django.contrib.auth.models import User

# Create your models here.
class HydroAreas(models.Model):
    name = models.CharField(max_length=22)
    lng = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    data_json = models.TextField()
    image = models.CharField(max_length=66, blank=True, null=True)

    def __str__(self):
        return self.name

class State(models.Model):
    name = models.CharField(max_length=32)
    capital = models.CharField(max_length=32, blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)

    def __str__(self):
        return self.name


class Lgas(models.Model):
    name = models.CharField(max_length=32, unique=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)
    hydro_area = models.ForeignKey(HydroAreas, on_delete=models.PROTECT, default=None)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class PredictionSearch(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT, default=None)
    lga = models.ForeignKey(Lgas, on_delete=models.PROTECT, default=None)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.lga


class Probable_Class(models.Model):
    name = models.CharField(max_length=30)
    color = models.CharField(max_length=11, blank=True, null=True)
    img = models.CharField(max_length=90, blank=True, null=True)  # Field name made lowercase.
    createdby = models.ForeignKey(User, on_delete=models.PROTECT, default=None)  # Field name made lowercase.
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Year(models.Model):
    year = models.IntegerField(unique=True)
    createdby = models.ForeignKey(User, on_delete=models.PROTECT, default=None)
    create_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.year)

class Predictions(models.Model):
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    lga = models.ForeignKey(Lgas, on_delete=models.PROTECT)
    prediction = models.ForeignKey(Probable_Class, on_delete=models.PROTECT)
    year = models.ForeignKey(Year, on_delete=models.PROTECT)
    actual_occurence = models.TextField(null=True, default=None)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True, default=None)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return str(self.lga.name)
