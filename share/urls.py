from django.urls import path, include
from rest_framework.routers import DefaultRouter
from share import views

router = DefaultRouter()
router.register(r'share', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
