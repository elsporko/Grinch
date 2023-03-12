from django.contrib import admin
from django.urls import path, include
from picklist.views import(Picklist, Picklists)

urlpatterns = [
    path('api/picklist/', Picklists.as_view()),
    path('api/picklist/<int:pk>/', Picklist.as_view())
]
