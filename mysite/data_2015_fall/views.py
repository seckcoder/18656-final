# Create your views here.
import urllib2
from datetime import datetime
from django.shortcuts import render
import simplejson
from django.utils.safestring import SafeString
from django.http import JsonResponse
from data_2015_fall.models import *
from neomodel import DoesNotExist

def landing(request):
    a = ""
    h = ""
    out = ""
    target = 'index.html'
    try:
      a = request.GET['input'].replace(" ", "%20")
      h = request.GET['search_param']
      req = urllib2.Request('http://127.0.0.1:8000/dblp/coauthors/' + h +'/'+a)
      f = urllib2.urlopen(req)
      out = f.read()
    except:
      pass

    if "Can't find Author" in out or not out:
     target = 'base.html'

    return render(request,
    target,
    {'out':SafeString(out)}
    )


def demo_wei(request):
    print "here"
    return JsonResponse({'foo': 'bar'})

def findCoAuthors_(name):
    author = Author.nodes.get(name=name)
    coauthors = set()
    for article in author.articles.all():
        for coauthor in article.authors.all():
            coauthors.add(coauthor)
    return coauthors

def findCoAuthors(request, name):
    try:
        coauthors = findCoAuthors_(name)
    except DoesNotExist as e:
        return JsonResponse({'error': "Can't find Author: " + name})
    return JsonResponse({'coauthors': simplejson.dumps([author.toDict() for author in coauthors])})


def dfs(level, depth, u, coauthors):
    coauthors.add(u)
    if level >= depth: return

    for v in findCoAuthors_(u.name):
        if not v in coauthors:
            dfs(level+1, depth, v, coauthors)

def findCoAuthorsMultiLevel_(depth, name):
    author = Author.nodes.get(name=name)
    coauthors = set()
    dfs(0, depth, author, coauthors)
    return coauthors

def findCoAuthorsMultiLevel(request, level, name):
    try:
        coauthors = findCoAuthorsMultiLevel_(level, name)
    except DoesNotExist as e:
        return JsonResponse({'error': "Can't find Author: " + name})
    return JsonResponse({'coauthors': simplejson.dumps([author.toDict() for author in coauthors])})
