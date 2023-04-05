from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    
    path('', TestAPIView.as_view(), name='test'),
]
