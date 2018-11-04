from django.contrib.auth.models import User, Group
from rest_framework import serializers
from mototaxi.apps.conductores.models import Conductor#, Moto

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ConductorSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Conductor
		fields=('id', 'nombre', 'identificacion','correo','celular')
"""
class MotoSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Moto
		fields=('id', 'placa', 'modelo')
"""