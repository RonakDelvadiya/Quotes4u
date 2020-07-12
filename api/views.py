from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken import views as tokenView
from rest_framework.decorators import api_view, authentication_classes
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from django.contrib.auth.models import User,UserManager
from rest_framework.views import APIView
from django.db.models import *
from datetime import datetime, date
from django.db.models import Q
from QuotesModel.serializers import *
from QuotesModel.models import *
import string
import datetime
import time
import re
import random
import csv


# User Regestration
class Regestration(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            uname = request.data['username']
            queryset = User.objects.all().filter(username=uname).exists()
            if queryset:
                return Response({'usererror': 'Username already exist'}, status=status.HTTP_200_OK)
            else:
                pwd = request.data['password']
                pass1 = pwd
                if re.match(r"^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])([a-zA-Z0-9]{8,15})$", pass1):
                    print "match"            
                    try:
                        rpwd = request.data['conform_password']    
                    except:
                        return Response({'error': 'add conform password'}, status=status.HTTP_200_OK)
                    try:
                        fname = request.data['first_name']    
                    except:
                        return Response({'error': 'add first_name'}, status=status.HTTP_200_OK)
                    try:
                        lname = request.data['last_name']    
                    except:
                        return Response({'error': 'add last_name'}, status=status.HTTP_200_OK)
                    try:
                        email = request.data['email']    
                    except:
                        return Response({'error': 'add email'}, status=status.HTTP_200_OK)
                    if (rpwd == pwd): 
                            fname = request.data['first_name']
                            lname = request.data['last_name']
                            email = request.data['email']
                            userdetails=serializer.save()
                            userdetails.set_password(request.data['password'])
                            userdetails.save()
                            return Response(serializer.data, status=status.HTTP_201_CREATED)
                    else:
                        return Response({'error': 'Your password and conform password both are not match'}, status=status.HTTP_200_OK)
                else:
                    print "not match"
                    return Response({'error': 'Your password must be more than 8 charcter ,atleast 1 digit,atleast 1 uppercase and atleast 1 lowercase '}, status=status.HTTP_200_OK)
        else:
        	return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Authers class
class Authors(APIView):
    authentication_classes = (TokenAuthentication,)
	
    def post(self, request, format=None):
        if request.user.is_authenticated():
            try:
                added_auther_name = request.data['name']
                checkduplicate = Author.objects.filter(name__icontains=added_auther_name).exists()
                print checkduplicate
                if checkduplicate :
                    print "duplicate"
                    return Response({'error': 'you are adding duplicate author'}, status=status.HTTP_200_OK)                   
                else:
                    print "unique"        
                    serializer = AuthorSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
    	            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            except:
                return Response({'error': "please add author's name"}, status=status.HTTP_200_OK)
             
        else:
            return Response({'error': 'You are not authenticated to add author'}, status=status.HTTP_200_OK)

    def get(self,request): 
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)


# Auther's details class
class Authors_details(APIView):
    authentication_classes = (TokenAuthentication,)

    def delete(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
	        	author = Author.objects.get(id=pk,)
	        except:
	        	return Response({'error': 'Author not found'}, status=status.HTTP_400_BAD_REQUEST)
	        author.delete()
	        return Response({'success': 'Author deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)

   def put(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
		        author = Author.objects.get(id=pk,)
	        except:
		        return Response({'error': 'author not found'}, status=status.HTTP_400_BAD_REQUEST)
	        serializer = AuthorSerializer(author, data=request.data, many=False)
	        if serializer.is_valid():
		        serializer.save()
		        return Response(serializer.data, status=status.HTTP_201_CREATED)
	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


# Categorys class
class Categorys(APIView):
    authentication_classes = (TokenAuthentication,)
	
    def post(self, request, format=None):               
        if request.user.is_authenticated():
            try:
                added_category = request.data['category']
                checkduplicate = Category.objects.filter(category__icontains=added_category).exists()
                print checkduplicate
                if checkduplicate :
                    print "duplicate"
                    return Response({'error': 'you are adding duplicate category'}, status=status.HTTP_200_OK)                   
                else:
                    print "unique"        
                    serializer = CategorySerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response(serializer.data, status=status.HTTP_201_CREATED)
    	            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                    
            except:
                return Response({'error': 'Add category'}, status=status.HTTP_200_OK)                   
        else:
            return Response({'error': 'You are not authenticated to add Category'}, status=status.HTTP_200_OK)            
            
    def get(self,request): 
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)


# Category details class
class Category_details(APIView):
    authentication_classes = (TokenAuthentication,)

    def delete(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
	        	category = Category.objects.get(id=pk,)
	        except:
	        	return Response({'error': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)
	        category.delete()
	        return Response({'success': 'Category deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)

    def put(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
		        category = Category.objects.get(id=pk,)
	        except:
		        return Response({'error': 'category not found'}, status=status.HTTP_400_BAD_REQUEST)
	        serializer = CategorySerializer(category, data=request.data, many=False)
	        if serializer.is_valid():
		        serializer.save()
		        return Response(serializer.data, status=status.HTTP_201_CREATED)
	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


# Occupation class
class Occupations(APIView):
    authentication_classes = (TokenAuthentication,)
	
    def post(self, request, format=None):
        if request.user.is_authenticated():
            print "in if "
            try:
                added_occupation = request.data['occupation']
                print "in try"
            except:
                print "in except"
                return Response({'error': 'Add Occupation'}, status=status.HTTP_200_OK)
            print "out of try catch"
            print added_occupation
            checkduplicate = Occupation.objects.filter(occupation__icontains=added_occupation).exists()            
            print checkduplicate
            if checkduplicate :
                print "duplicate"
                return Response({'error': 'you are adding duplicate Occupation'}, status=status.HTTP_200_OK)                   
            else:
                print "unique"        
                serializer = OccupationSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
    	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                                
        else:
            return Response({'error': 'You are not authenticated to add Occupation'}, status=status.HTTP_200_OK)

    def get(self,request): 
        occupation = Occupation.objects.all()
        serializer = OccupationSerializer(occupation, many=True)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)


# Occupation's details class
class Occupation_details(APIView):
    authentication_classes = (TokenAuthentication,)

    def delete(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
	        	occupation = Occupation.objects.get(id=pk,)
	        except:
	        	return Response({'error': 'Category not found'}, status=status.HTTP_400_BAD_REQUEST)
	        occupation.delete()
	        return Response({'success': 'Category deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
		        occupation = Occupation.objects.get(id=pk,)
	        except:
		        return Response({'error': 'occupation not found'}, status=status.HTTP_400_BAD_REQUEST)
	        serializer = OccupationSerializer(occupation, data=request.data, many=False)
	        if serializer.is_valid():
		        serializer.save()
		        return Response(serializer.data, status=status.HTTP_201_CREATED)
	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


# Quotes class
class Quote(APIView):
    authentication_classes = (TokenAuthentication,)
	
    def post(self, request, format=None):
        if request.user.is_authenticated():
            print "in if "
            try:
                added_quote = request.data['quote']
            except:
                return Response({'error': 'Add Quote'}, status=status.HTTP_200_OK)
            try:
                added_auther = request.data['authorid']
            except:
                return Response({'error': 'Add auther'}, status=status.HTTP_200_OK)
            try:
                added_category = request.data['category']
            except:
                return Response({'error': 'Add category'}, status=status.HTTP_200_OK)
            checkduplicate = Quotes.objects.filter(quote__icontains=added_quote).exists()            
            print checkduplicate
            if checkduplicate :
                print "duplicate"
                return Response({'error': 'you are adding duplicate Quote'}, status=status.HTTP_200_OK)                   
            else:
                print "unique"        
                serializer = QuoteSerializer(data=request.data)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
    	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)                                
        else:
            return Response({'error': 'You are not authenticated to add quote'}, status=status.HTTP_200_OK)

    def get(self,request): 
        quotes = Quotes.objects.all()
        serializer = QuoteSerializer(quotes, many=True)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)


# Quote's details class
class Quote_details(APIView):
    authentication_classes = (TokenAuthentication,)

    def delete(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
	        	quotes = Quotes.objects.get(id=pk,)
	        except:
	        	return Response({'error': 'quote not found'}, status=status.HTTP_400_BAD_REQUEST)
	        quotes.delete()
	        return Response({'success': 'quotes deleted successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


    def put(self, request, pk, format=None):
        if request.user.is_authenticated():
	        try:
		        quotes = Quotes.objects.get(id=pk,)
	        except:
		        return Response({'error': 'quote not found'}, status=status.HTTP_400_BAD_REQUEST)
	        serializer = QuoteSerializer(quotes, data=request.data, many=False)
	        if serializer.is_valid():
		        serializer.save()
		        return Response(serializer.data, status=status.HTTP_201_CREATED)
	        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'You are not authenticated'}, status=status.HTTP_200_OK)


# 1). all filters
class Get_search_all(APIView):
    def get(self,request):
        try:
            get_author=request.GET['author']
        except:
            get_author=0
        try:
            get_category=request.GET['category']
        except:
            get_category=0    
        if ((get_author == 0) & (get_category == 0)):
            allquotelist = Quotes.objects.all()
            serializer = QuoteSerializer(allquotelist,many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)     
        else:
            print get_author
            if ((get_category != 0) & (get_author == 0)):
                filterd_quote_list = Quotes.objects.filter( Q(category__id=get_category))
                print (filterd_quote_list)             
                serializer = QuoteSerializer(set(filterd_quote_list),many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            if get_category == 0 : 
                filterd_quote_list = Quotes.objects.filter(Q(authorid__id=get_author))
                print (filterd_quote_list)             
                serializer = QuoteSerializer(set(filterd_quote_list),many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                filterd_quote_list = Quotes.objects.filter(Q(authorid__id=get_author) & Q(category__id=get_category))
                print (filterd_quote_list)             
                serializer = QuoteSerializer(set(filterd_quote_list),many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)


class Load_autosearch_suggestion(APIView):
    def get(self,request):
        reader = csv.DictReader(open(file_path))
        for row in reader:
            author_name = Author(name=row['Name'])
            author_name.save()


class Get_authors(APIView):
    def get(self,request):
        if request.is_ajax():
            q = request.GET.get('term', '')
            authors = Author.objects.filter(name__icontains = q )[:20]
            results = []
            for author in authors:
                authors_json = {}
                authors_json['name'] = author.name
                
                
                results.append(authors_json)
            data = json.dumps(results)
        else:
            data = 'fail'
        mimetype = 'application/json'
        return HttpResponse(data, mimetype)
        

class RandomQuote(APIView):
    def get(self,request):
        quotelist = Quotes.objects.values_list('id').all()
        print quotelist
        n = random.randint(1,len(quotelist)) # returns a random integer
        quotes = Quotes.objects.filter(id=n)
        serializer = QuoteSerializer(quotes, many=True)
        print serializer.data
        return Response(serializer.data, status=status.HTTP_200_OK)