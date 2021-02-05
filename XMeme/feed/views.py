from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import *
from .serializers import *

def index(request):
    return HttpResponse("Hello, world. You're at the feed index.")

class MemeList(generics.ListCreateAPIView):
    queryset = Meme.objects.all().order_by('-id')[:100]
    serializer_class = MemeSerializer

class OwnerList(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class MemeDetails(generics.RetrieveUpdateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

class OwnerDetails(generics.RetrieveUpdateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer