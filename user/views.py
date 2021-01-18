from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import detailsSerializer
from .models import details
from django.http import HttpResponse
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework import serializers

@api_view(['GET'])
def home(request):
    api_urls ={
     'List':'/show/',
     'view':'/view/',



        }
    return Response(api_urls)




@api_view(['GET'])

def show(request):
    detail=details.objects.all()
    serializer=detailsSerializer(detail,many=True)
    return Response(serializer.data)

def view(request):
        if request.method=='GET':
             obj=details.objects.all()
             return render (request,'index.html',{"obj":obj})
        else:
               return render (request,'index.html')



