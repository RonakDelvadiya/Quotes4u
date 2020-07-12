from django.conf.urls import patterns, include, url
from django.contrib import admin
from api import views
from rest_framework.authtoken import views as tokenView


urlpatterns = patterns('',
    url(r'^login/$',tokenView.obtain_auth_token),
    url(r'^user_register/', views.Regestration.as_view()),
    url(r'^author/', views.Authors.as_view()),
    url(r'^author_details/(?P<pk>[0-9]+)/$', views.Authors_details.as_view()),
    url(r'^category/', views.Categorys.as_view()),
    url(r'^category_details/(?P<pk>[0-9]+)/$', views.Category_details.as_view()),
    url(r'^occupation/', views.Occupations.as_view()),
    url(r'^occupation_details/(?P<pk>[0-9]+)/$', views.Occupation_details.as_view()),
    url(r'quotes/', views.Quote.as_view()),
    url(r'^quote_details/(?P<pk>[0-9]+)/$', views.Quote_details.as_view()),
    url(r'getsearch/', views.Get_search_all.as_view()),
    url(r'getrandomquote/', views.RandomQuote.as_view()),
    url(r'^api/get_authors/',  views.Get_authors.as_view(), name='    '),
)