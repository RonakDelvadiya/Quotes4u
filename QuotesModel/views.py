from django.shortcuts import render, Http404
from django.http import HttpResponseRedirect
from .models import *
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse
from django.contrib.auth import logout
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import *
from rest_framework import status
from rest_framework import filters
from rest_framework import generics
import random
from django.db.models import Q
import os
import json
import csv
from django.utils.encoding import smart_str, smart_unicode
import  ast


def QuoteList(request):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    a =[allquotelist1[random.randrange(len(allquotelist1))]for item in range(33)]
    idofquote = random.choice(allquotelist1)
    quotelist = Quotes.objects.filter(id__in=a)
    randomquoteslist = Quotes.objects.get(id=idofquote)    
    return render(request, 'QuotesModel/index.html',{'quotes':quotelist ,'randomquotes':randomquoteslist})


def GoToAuthor(request):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    idofquote = random.choice(allquotelist1)
    randomquote = Quotes.objects.get(id=idofquote)      
    authorlist = Author.objects.all().order_by('name')
    return render(request, 'QuotesModel/author.html',{'authorlist':authorlist, 'randomquote':randomquote})


def GoToCategory(request):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    idofquote = random.choice(allquotelist1)
    randomquote = Quotes.objects.get(id=idofquote)      
    categorylist = Category.objects.all().order_by('category')
    return render(request, 'QuotesModel/category.html',{'categorylist':categorylist,'randomquote':randomquote})


def GetQuotesByCategory(request,pk):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    categorywisequotelist = Quotes.objects.filter(category__id=pk)
    getnameofcategory = Category.objects.get(id=pk)
    a=True
    allquoteidlist = Quotes.objects.values_list('id').all()
    idofquote = random.choice(allquotelist1)
    randomquoteslist = Quotes.objects.get(id=idofquote)      
    return render(request, 'QuotesModel/searchpage.html',{'categoryname':getnameofcategory ,'randomquotes':randomquoteslist ,'categorywisequotes':categorywisequotelist , 'categoryflag':a})


def GetQuotesByAuthor(request,pk):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    authorwisequotelist = Quotes.objects.filter(authorid=pk)
    getnameofauthor = Author.objects.get(id=pk)
    b=True
    allquoteidlist = Quotes.objects.values_list('id').all()
    idofquote = random.choice(allquotelist1)
    randomquoteslist = Quotes.objects.get(id=idofquote)     
    return render(request, 'QuotesModel/searchpage.html',{'authername':getnameofauthor ,'randomquotes':randomquoteslist ,'authorwisequotes':authorwisequotelist ,'authorflag':b})



def GiveSearchResultOfAuthor(request):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    a =[allquotelist1[random.randrange(len(allquotelist1))]for item in range(33)]
    quotelist=Quotes.objects.filter(id__in=allquotelist1)
    c=True
    allquoteidlist = Quotes.objects.values_list('id').all()
    idofquote = random.choice(allquotelist1)
    randomquoteslist = Quotes.objects.get(id=idofquote)     

    if request.method == 'POST':
        searchdeatils=request.POST
        authorname = searchdeatils.get('author')
        if authorname=="" :
            return render(request, 'QuotesModel/searchpage.html',{'quotes':quotelist,'randomquotes':randomquoteslist })
        getquotes = Quotes.objects.filter(authorid__name__icontains=authorname,)   
        if getquotes :
            return render(request, 'QuotesModel/searchpage.html',{'authorname':authorname,'filterdquotes':set(getquotes) ,'randomquotes':randomquoteslist ,'searchflag' :c })
    return render(request, 'QuotesModel/searchpage.html',{'error':"Oppess..  we dont have any quotes.",})



def GiveSearchResultOfCategory(request):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    a =[allquotelist1[random.randrange(len(allquotelist1))]for item in range(9)]
    quotelist=Quotes.objects.filter(id__in=allquotelist1)
    c=True
    allquoteidlist = Quotes.objects.values_list('id').all()
    idofquote = random.choice(allquotelist1)
    randomquoteslist = Quotes.objects.get(id=idofquote)     
    if request.method == 'POST':
        searchdeatils=request.POST
        categoryname = searchdeatils.get('category')
        if categoryname=="" :
            return render(request, 'QuotesModel/searchpage.html',{'quotes':quotelist,'randomquotes':randomquoteslist })
        getquotes = Quotes.objects.filter(category__category__icontains=categoryname)   
        if getquotes :
            return render(request, 'QuotesModel/searchpage.html',{'catename':categoryname,'filterdquotes':set(getquotes) ,'randomquotes':randomquoteslist ,'searchflag' :c })
    return render(request, 'QuotesModel/searchpage.html',{'error':"Oppess..  we dont have any quotes.",})


def GiveSearchResult(request):
    allquotelist1 = Quotes.objects.values_list('id',flat=True).all()
    a =[allquotelist1[random.randrange(len(allquotelist1))]for item in range(9)]
    quotelist=Quotes.objects.filter(id__in=allquotelist1)
    c=True
    allquoteidlist = Quotes.objects.values_list('id').all()
    idofquote = random.choice(allquotelist1)
    randomquoteslist = Quotes.objects.get(id=idofquote)     

    if request.method == 'POST':
        searchdeatils=request.POST
        categoryname = searchdeatils.get('category')
        authorname = searchdeatils.get('author')
        if authorname=="" and categoryname=="" :
            return render(request, 'QuotesModel/searchpage.html',{'quotes':quotelist,'randomquotes':randomquoteslist })
        getquotes = Quotes.objects.filter(authorid__name__icontains=authorname,category__category__icontains=categoryname)   
        if getquotes :
            return render(request, 'QuotesModel/searchpage.html',{'authorname':authorname,'catename':categoryname,'filterdquotes':set(getquotes) ,'randomquotes':randomquoteslist ,'searchflag' :c })
    return render(request, 'QuotesModel/searchpage.html',{'error':"Oppess..  we dont have any quotes.",})


def adddata(request):
    sourceFile = open(os.path.join("QuotesModel","quotes.json",))
    json_data = json.load(sourceFile)
    outputFile = open("quotes.csv" , "w")
    outputWriter = csv.writer(outputFile)
    featurelist = []
    print type(json_data)
    for data in json_data:
        list1=[]
        quotes = data['quote']
        author = data['author']
        categorys = data['category']
      
        getauthorid=Author.objects.get_or_create(name=author)
        for cate in categorys:
        
            getcategoryid=Category.objects.values_list('id',flat=True).get_or_create(category=cate)
        
            list1.append(getcategoryid[0])

        cretatequote=Quotes.objects.create(authorid=getauthorid[0],quote=quotes)
        try:
            cretatequote.category.add(list1[0],)
        except Exception as e:
            print e
            continue
        try:
            cretatequote.category.add(list1[1],)
        except Exception as e:
            print e
            continue

        try:
            cretatequote.category.add(list1[2],)
        except Exception as e:
            print e
            continue
        cretatequote.save()