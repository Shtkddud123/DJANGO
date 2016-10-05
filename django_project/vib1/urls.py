from django.conf.urls import url
from . import views 
urlpatterns = [
    url(r'^$', views.index, name='index'), ## This is the homepage that is associated with ScienceBlogs (This is the default)    
] 
