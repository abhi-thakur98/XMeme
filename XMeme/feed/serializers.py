from django.db.models import fields
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import *

class OwnerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Owner
		fields = '__all__'
class MemeSerializer(serializers.ModelSerializer):
	owner = serializers.StringRelatedField()
	class Meta:
		model = Meme
		fields = ['id','owner','url','caption']
		validators = [
            UniqueTogetherValidator(
                queryset=Meme.objects.all(),
                fields=['owner', 'caption','url'],
				message = 'Duplicate Data'
            )
        ]