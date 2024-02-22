from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.urls import re_path

from users.views import GrinchUserView, GrinchUserRegisterView, GrinchUserLoginView, GrinchUserLogoutView
from picklist.views import (RouteViewSet, RoutesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("picklist.urls")),
    path('register/', GrinchUserRegisterView.as_view(), name='register'),
    path('login/', GrinchUserLoginView.as_view(), name='login'),
    path('logout/', GrinchUserLogoutView.as_view(), name='logout'),
    path('api/users/', GrinchUserView.as_view(), name='user'),
    path('api/users/<int:id>', GrinchUserView.as_view(), name='users'),
    path('api/routes/', RoutesViewSet.as_view(), name='routes'),
    path('api/routes/<str:pk>/', RouteViewSet.as_view(), name='route'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
