from django.conf.urls import url

from working.views import *

urlpatterns = [

    url('^index',index,name="index")
]