from django.contrib import admin
from django.urls import path, include
from picklist.views import(PicklistViewSet, PicklistsViewSet)

urlpatterns = [
    path('api/picklist/', PicklistsViewSet.as_view()),
    path('api/picklist/<int:pk>/', PicklistViewSet.as_view())
]
