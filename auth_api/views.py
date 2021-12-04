from auth_api.serializer import SignInSerializer, SignUpSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

@api_view(['POST'])
def signIn(request):

    username = request.data["username"]
    password = request.data["password"]

    logout(request)

    try:
        user_auth = authenticate(request, username=username, password=password)
        login(request, user_auth)

        if request.user.is_authenticated:
            data = User.objects.get(username=username)
            data_serializer = SignInSerializer(data, many=False)
            return Response(data_serializer.data)

    except: return "error"

@api_view(['POST'])
def signUp(request):
    data_serializer = SignUpSerializer(data=request.data)

    if data_serializer.is_valid():
        data_serializer.save()
        return Response(data_serializer.data)
    
    return Response(data_serializer.errors)