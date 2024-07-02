from django.urls import path
# '.' means current folder
from . import views

#
# /products/1/detail
# /products/new

urlpatterns = [
    path('', views.index),
    path('new', views.new)
]