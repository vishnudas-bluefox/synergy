#!/usr/bin/env python3

from rest_framework import serializers

#import the models here
from .models import user,usertable,kseb,transactionlog


class userserializer(serializers.ModelSerializer):
    class Meta:
        model = user
        fields = ['id','name','consumerno','email','password']
        extra_kwargs = {
            "password" : {'write_only':True}
        }

    #hash the password
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class usertableserializer(serializers.ModelSerializer):
    class Meta:
        model = usertable
        fields = ['id','consumerno','name','bpoint','tcredit','ucredit','monthlycap']


class ksebserializer(serializers.ModelSerializer):
    class Meta:
        model = kseb
        fields = ['consumerno','solarcapacity']


class transactionserializer(serializers.ModelSerializer):
    class Meta:
        model = transactionlog
        fields = ['sender','receiver','amount']
