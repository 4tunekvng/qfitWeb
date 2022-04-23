from rest_framework import serializers
from .models import Data
from .models import Feature

class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ('id', 'title')

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        fields = ('id','title', 'values', 'data')

