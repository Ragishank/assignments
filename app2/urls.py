
from django.urls import path
from . import views

urlpatterns = [
   path('',views.f1,name='text'),
   path('1',views.f2,name='text2'),
   path('first',views.f3,name='text')
]
