from django.conf.urls import url

from adminApp.views import *

urlpatterns = [


    url("^index$",index,name="index"),



]