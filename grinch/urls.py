from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
# from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.urls import re_path

from users.views import GrinchUserView
from picklist.views import (RouteViewSet, RoutesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("picklist.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/users/', GrinchUserView.as_view(), name='home'),
    path('api/routes/', RoutesViewSet.as_view(), name='allroutes'),
    path('api/routes/<str:pk>/', RouteViewSet.as_view(), name='routes'),
]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
