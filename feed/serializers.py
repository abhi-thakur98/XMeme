from rest_framework import serializers
from .models import *

class OwnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Owner
		fields = '__all__'

class MemeSerializer(serializers.ModelSerializer):
	name = serializers.StringRelatedField()
	class Meta:
		model = Meme
		fields = ['id','name','url','caption']