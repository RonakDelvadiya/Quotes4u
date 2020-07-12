from django.conf.urls import url
from .views import *
from django.contrib.auth.decorators import login_required
from django.conf.urls import include


urlpatterns = [
    url(r'^$', QuoteList, name='index'),
    url(r'^category/(?P<pk>[0-9]+)$', GetQuotesByCategory),
    url(r'^author/(?P<pk>[0-9]+)$', GetQuotesByAuthor),
    url(r'^search/$', GiveSearchResult),
    url(r'^author/$', GoToAuthor),
    url(r'^category/$', GoToCategory),
    url(r'^searchcategory/$', GiveSearchResultOfCategory),
    url(r'^searchauthor/$', GiveSearchResultOfAuthor),
    url(r'^adddata/$', adddata),    
]