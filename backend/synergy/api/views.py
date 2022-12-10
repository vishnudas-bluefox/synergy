from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import user,usertable,kseb
from .serializers import userserializer,usertableserializer,ksebserializer

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
        response ={}
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
        #create user table for handling the points and other details
        response["s1"]=serializer.data
        consumerno =  request.query_params.get("consumerno")
        name = request.query_params.get("name")
        user_table={}
        user_table["consumerno"]=consumerno
        user_table["name"]=name
        try:
            serializer2 = usertableserializer(data=user_table)
        except Exception as e:
            print("Error",e)
        serializer2.is_valid(raise_exception=True)
        serializer2.save()
        response["s2"]=serializer2.data


        return Response(response)


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

# add solar capacity to kseb table by consumerno
class kseb_solarvalue(APIView):
    def post(self,request):
        consumerno = request.query_params.get("consumerno")
        solarcapacity = request.query_params.get("solarcapacity")
        solar_data ={}
        solar_data["consumerno"]=consumerno
        solar_data["solarcapacity"]=solarcapacity
        kseb_detail = kseb.objects.filter(consumerno=consumerno).first()
        if kseb_detail is not None:
            return AuthenticationFailed("User already have the solar capacity limit")
        serializer = ksebserializer(data=solar_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        #updating the monthly capital
        user_table_details = usertable.objects.filter(consumerno=consumerno).first()
        if user_table_details is None:
            return AuthenticationFailed("Consumer dosen't seen in table try different consumerID")
        user_table_details.monthlycap = solarcapacity
        user_table_details.save()
        print("User monthly capacity updated")

        return Response(serializer.data)


kseb_solarvalue = kseb_solarvalue.as_view()

#add consumer points
class addpoints(APIView):
    def post(self,request):
        consumerno = request.query_params.get("consumerno")
        points = request.query_params.get("points")
        point_data = {}
        point_data["consumerno"] = int(consumerno)
        point_data["points"] = int(points)
        print(point_data)
        user_table_details = usertable.objects.filter(consumerno=consumerno).first()
        if user_table_details is None:
            return AuthenticationFailed("The user not found try to register the user.")
        try:
            user_table_details.bpoint = user_table_details.bpoint+int(points)
            user_table_details.save()
            serializer = usertableserializer(user_table_details)
        except Exception as e:
            print("Data saving part:",e)

        return Response(serializer.data)

addpoints = addpoints.as_view()

#retrive user data using consumer no
class user_detail(APIView):
    def get(self, request):
        consumerno = request.query_params.get("consumerno")
        user_table_detail = usertable.objects.filter(consumerno=consumerno).first()
        serializer = usertableserializer(user_table_detail)
        return Response(serializer.data)

userdata = user_detail.as_view()
