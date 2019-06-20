from django.conf.urls import  url

from .views import *

urlpatterns =[
    url(r'Register/$',Saving.as_view()),
    url(r'get/$',Fetch.as_view()),
    url(r'one/$',Fetchingonedata.as_view()),
    url(r'editing/$',Editingdata.as_view()),
    url(r'del/$', Removedata.as_view())
]