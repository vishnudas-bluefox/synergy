from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import user
from .serializers import userserializer

import datetime
import jwt

# Create your views here.

@api_view(['GET'])
def test(request,*args,**kwargs):
    return Response({"Message":"Success"})


class classtest(APIView):
    def get(self,request):
        print(request.query_params.get("message"))
        return Response({"Mesage":"Get to hell"})
classtest =classtest.as_view()

class registerview(APIView):
    def post(self,request):
        name = request.query_params.get("name")
        consumerno = request.query_params.get("consumerno")
        email = request.query_params.get("email")
        password = request.query_params.get("password")

        user_cred = {}
        user_cred["name"]=name
        user_cred["consumerno"]=consumerno
        user_cred["email"]=email
        user_cred["password"]=password
        serializer = userserializer(data=user_cred)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


registerview =registerview.as_view()


class login(APIView):
    def post(self,request):
        email = request.query_params.get("email")
        password = request.query_params.get("password")

        user_detail = user.objects.filter(email=email).first()
        if user_detail is None:
            raise AuthenticationFailed("User not found")
        if not user_detail.check_password(password):
            raise AuthenticationFailed("Incorrect password")
        #payload for reating cookiee
        payload = {
            'id': user_detail.id,
            'email':email,
            'password': password,
            'consumerno' : user_detail.consumerno,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1),
            'iat': datetime.datetime.utcnow()
        }
        #creating jwt toke using payload
        token = jwt.encode(payload,'secret',algorithm='HS256')

        #Creating cookie and returning the token as response also
        response = Response()
        response.set_cookie(key='token',value=token, httponly=True)
        response.data = {
            "Message":"Authentication Succesfull",
            "token": token
        }

        return response


loginview = login.as_view()
