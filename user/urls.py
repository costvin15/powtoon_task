from django.urls import path, include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from user import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    url(r'auth/login', obtain_jwt_token),
    url(r'auth/register/', include('rest_auth.registration.urls'))
]
