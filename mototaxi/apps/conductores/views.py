from rest_framework import generics
from mototaxi.apps.conductores.models import Conductor#, #Moto
from mototaxi.apps.conductores.serializers import ConductorSerializer#, MotoSerializer

class ConductorList(generics.ListCreateAPIView):
	queryset=Conductor.objects.all()
	serializer_class=ConductorSerializer

class ConductorDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset= Conductor.objects.all()
	serializer_class=ConductorSerializer
"""
class MotoList(generics.ListCreateAPIView):
	queryset=Moto.objects.all()
	serializer_class=MotoSerializer

class MotoDetail(generics.RetrieveUpdateDestroyAPIView):
	queryset= Moto.objects.all()
	serializer_class=MotoSerializer
"""