from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import MyUser
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        data = request.data
        email = data['email']
        password = data['password']
        c_password = data['c_password']
        if password == c_password:
            obj = MyUser(email = email, password = password, c_password = c_password)
            obj.save()
        return Response({"staus":200})

class SiginView(APIView):
    def post(self,request):
        data = request.data
        email = data['email']
        password = data['password']
        user= MyUser.objects.get(email = email, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            print(refresh)
            return Response({"status":200,
                         "refresh": str(refresh),
            "access": str(refresh.access_token)
            })

        return Response({"staus":404})
    

class TestUser(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user.email
        print("user email is",user)
        return Response({"status":200})
