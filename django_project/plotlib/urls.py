from django.conf.urls import url
from . import views 
# instead of creating the regular expression/website combo in the root project directory url.py, we add it to it's individual
# folder

urlpatterns = [
    url(r'^$', views.showimage, name='showimage'), ## This is the homepage that is associated with ScienceBlogs (This is the default)    
] 
