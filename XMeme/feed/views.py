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
        serializer = MemeSerializer(data=request.data)

        if serializer.is_valid():
            owner = get_object_or_404(Owner, pk=request.data.get('owner'))
            owner.num_memes += 1
            owner.save()
            serializer.save()
            return Response({"id" : serializer.data.get('id')},status=201)
        return Response(serializer.data,status=422)
        
class OwnerList(generics.ListCreateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer

class MemeDetails(generics.RetrieveUpdateAPIView):
    queryset = Meme.objects.all()
    serializer_class = MemeSerializer

    def update(self, request, *args, **kwargs):
        meme = get_object_or_404(Meme, pk=request.data.get('id'))
        owner = request.data.get('owner')
        if owner and meme.owner.id != owner:
            return HttpResponse(status=400)

        serializer = MemeSerializer(instance=meme,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.data,status=422)

class OwnerDetails(generics.RetrieveUpdateAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer