from django.urls import path
from .views import *

urlpatterns = [
    path('', todolist, name="list"),
    path('create/', todocreate, name="create"),
    path('update/<str:pk>/', todoupdate, name="update"),
    path('delete/<str:pk>/', tododelete, name="delete")
]
