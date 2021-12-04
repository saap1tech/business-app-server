from rest_framework.decorators import api_view
from rest_framework.response import Response
from base_app.serializer import FilmSerializer, ProductSerializer, ServiceSerializer
from base_app.models import Film, Product, Service
from django.shortcuts import render

# Create your views here.

@api_view(["GET"])
def getFilms(request):
    data = Film.objects.all()
    data_serializer = FilmSerializer(data, many=True)
    return Response(data_serializer.data)

@api_view(["GET"])
def getServices(request):
    data = Service.objects.all()
    data_serializer = ServiceSerializer(data, many=True)
    return Response(data_serializer.data)

@api_view(["GET"])
def getProducts(request):
    data = Product.objects.all()
    data_serializer = ProductSerializer(data, many=True)
    return Response(data_serializer.data)