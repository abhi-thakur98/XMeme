from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from rest_framework import generics
from rest_framework.response import Response
from .models import *
from .serializers import *

def index(request):
    return render(request,'index.html')

class MemeList(generics.ListCreateAPIView):
    queryset = Meme.objects.all().order_by('-id')[:100]
    serializer_class = MemeSerializer

    def create(self, request, *args, **kwargs):
        name = request.data.get('name')
        url = request.data.get('url')
        caption = request.data.get('caption')
        
        try:
            owner,_ = Owner.objects.get_or_create(name=name)
            meme,created = Meme.objects.get_or_create(name=owner,url=url,caption=caption)
        except:
            return Response(status=422)
        
        if not created:
            return Response({"error" : "Duplicate"},status=422)
        owner.num_memes += 1
        owner.save()
        return Response({"id" : meme.id},status=201)
        
class OwnerList(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class MemeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        meme = get_object_or_404(Meme, pk=request.data.get('id'))
        name = request.data.get('name')
        if name and meme.owner.name != name:
            return Response(status=422)

        serializer = MemeSerializer(partial=partial,instance=meme,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=200)
        return Response(status=422)

class OwnerDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer