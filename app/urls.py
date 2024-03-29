"""powtoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
   openapi.Info(
      title="Powtoon API",
      default_version='v1',
      contact=openapi.Contact(email="costacastrovinicius7@gmail.com"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', include('user.urls')),
    path('', include('powtoon.urls')),
    path('', include('share.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('redoc-old/', schema_view.with_ui('redoc-old', cache_timeout=0), name='schema-redoc-old'),
]
