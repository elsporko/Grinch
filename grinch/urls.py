from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views
# from django.conf.urls.static import static
from django.conf import settings
# from django.contrib.staticfiles import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.urls import re_path

from users.views import GrinchUserViewSet, GrinchUserRegisterView, GrinchUserLoginView, GrinchUserLogoutView
from route.views import (RouteViewSet)

from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from picklist.views import PicklistViewSet

router = DefaultRouter()
router.register(r'routes', RouteViewSet, basename='routes')
router.register(r'picklists', PicklistViewSet, basename='picklists')
router.register('users', GrinchUserViewSet, basename='users')

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('register/', GrinchUserRegisterView.as_view(), name='register'),
    path('login/', GrinchUserLoginView.as_view(), name='login'),
    path('logout/', GrinchUserLogoutView.as_view(), name='logout'),

   # Schema endpoint (raw OpenAPI JSON)
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional Swagger UI
    path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # Optional ReDoc UI
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),


]


if settings.DEBUG:
    urlpatterns += staticfiles_urlpatterns()
