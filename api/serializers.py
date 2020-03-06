from rest_framework import serializers
from cms.models import *
from users.models import *
from predictions.models import *

class PageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = '__all__'


class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class LgaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lgas
        fields = '__all__'


class LgasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lgas#.StringRelatedField(many=True)
        fields = ['id', 'name', 'lat', 'lng', 'state', 'hydro_area', ]


class MenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'

class SubMenuSerializers(serializers.ModelSerializer):
    class Meta:
        model = Submenu
        fields = '__all__'

class HydroAreasSerializers(serializers.ModelSerializer):
    class Meta:
        model = HydroAreas
        fields = '__all__'

class ProbableClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Probable_Class
        fields = '__all__'

class PredictionsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Predictions
        fields = '__all__'

class StoriesClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Stories
        fields = '__all__'
