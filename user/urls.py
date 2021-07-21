from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from user import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'auth/', include('rest_auth.urls')),
    url(r'auth/register/', include('rest_auth.registration.urls'))
]
