from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DataSerializer,FeatureSerializer
from .models import Data, Feature


# Create your views here.

class DataView(viewsets.ModelViewSet):
    serializer_class = DataSerializer
    queryset = Data.objects.all()

class FeatureView(viewsets.ModelViewSet):
    serializer_class = FeatureSerializer
    queryset = Feature.objects.all()

