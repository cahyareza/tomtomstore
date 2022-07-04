# myproject/apps/ideas/urls.py
from django.urls import path
from .views import TestiList

urlpatterns = [
    path("testimoni/", TestiList.as_view(), name=TestiList.name),
]