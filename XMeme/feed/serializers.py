from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
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
		validators = [
            UniqueTogetherValidator(
                queryset=Meme.objects.all(),
                fields=['name', 'caption','url'],
				message = 'Duplicate Data'
            )
        ]