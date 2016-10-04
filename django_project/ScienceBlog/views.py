from django.shortcuts import render
from django.http import HttpResponse ## Standard website response you want
from django.http import HttpResponseNotFound
from .models import Science 
import datetime
## html css loader
from django.template import loader 


# getting from urls.py = "views.index" - so now, we have to write a index function!
def index(request):    
    now = datetime.datetime.now()
    all_Science = Science.objects.all() # same as in the shell - we ne
    template = loader.get_template('ScienceBlog/index.html')
    context = {
        'all_Science' : all_Science, # adding the context for the sql database 
    }
    return HttpResponse(template.render(context,request))
   
def detail(request, Science_id):
    return HttpResponse("<h2>Details for ScienceBlog later" + str(Science_id) + "</h2>") 
    
