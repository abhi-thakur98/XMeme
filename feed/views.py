from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *
import validators
import re

def index(request):
    return render(request,'index.html')

class MemeList(generics.ListCreateAPIView):
    queryset = Meme.objects.all().order_by('-id')
    serializer_class = MemeSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        url = request.data.get('url')
        caption = request.data.get('caption')

        if not validators.url(url):
            return Response({"detail":"ERROR : Invalid URL"},status=422)
        
        if not re.search(r'[a-zA-Z]',name):
            return Response({"detail":"ERROR : Invalid Name"},status=422)

        try:
            owner,_ = Owner.objects.get_or_create(name=name)
            meme,created = Meme.objects.get_or_create(name=owner,url=url,caption=caption)
        except:
            return Response({"detail":"ERROR : Unknown Error"},status=422)
        else:
            if not created:
                return Response({"detail":"ERROR : Duplicate Data"},status=409)
        
        owner.num_memes += 1
        owner.save()
        return Response({"id" : meme.id},status=201)

class OwnerList(generics.ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class MemeDetails(generics.RetrieveUpdateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        meme = get_object_or_404(Meme, pk=request.data.get('id'))
        name = request.data.get('name')
        url = request.data.get('url')
        if name and meme.name.name != name:
            return Response({"detail":"ERROR : Name Change Not Alowed"},status=422)

        if not validators.url(url):
            return Response({"detail":"ERROR : Invalid URL"},status=422)

        serializer = MemeSerializer(partial=partial,instance=meme,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"detail":"Success"},status=200)
        return Response({"detail":"ERROR : Duplicate Data"},status=409)