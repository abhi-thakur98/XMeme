from django.db.models import fields
from rest_framework import serializers
from .models import *

class MemeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Meme
		fields = '__all__'

class OwnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Owner
		fields = '__all__'