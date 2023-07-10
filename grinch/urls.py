from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

from users import views as user_views
from picklist import views as picklist_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("picklist.urls")),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('api/users/', user_views.GrinchUser.as_view(), name='home'),
    path('api/routes/', picklist_views.Routes.as_view(), name='routes')
]
