from rest_framework.response import Response
from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate, login, logout


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','first_name','last_name','username', 'email', 'password')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        exclude = ('created_at', 'modified_at','occupationid','id')  


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ('created_at', 'modified_at','id')    


class OccupationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Occupation
        exclude = ('created_at', 'modified_at','id')  


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quotes
        exclude = ('created_at', 'modified_at',)    