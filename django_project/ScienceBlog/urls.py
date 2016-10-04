from django.conf.urls import url
from . import views 
# instead of creating the regular expression/website combo in the root project directory url.py, we add it to it's individual
# folder

urlpatterns = [
    # /ScienceBlog/
    url(r'^$', views.index, name='index'), ## This is the homepage that is associated with ScienceBlogs (This is the default)    
    # /ScienceBlog/1/ - gives the database accoridng the keyid 1
    url(r'^(?P<Science_id>[0-3]+)/$', views.detail, name = 'detail'), # look between databsae id 0 - 3 range
] 
