from django.urls import path
from .views import *

urlpatterns = [
    path('home/', chat_view, name="home"),
]