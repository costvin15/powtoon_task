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

from django.urls import path
from . import views

urlpatterns = [
    path('user/create', views.user_create, name='user_create'),
    path('user/read/<int:user_id>', views.user_read, name='user_read'),
    path('powtoon/create', views.powtoon_create, name='powtoon_create'),
    path('powtoon/read/<int:user_id>', views.powtoon_read, name='powtoon_read'),
    path('powtoon/find/<int:user_id>/<int:powtoon_id>', views.powtoon_find_by_id, name='powtoon_find_by_id'),
    path('powtoon/edit/<int:user_id>/<int:powtoon_id>', views.powtoon_edit, name='powtoon_edit'),
    path('powtoon/delete/<int:user_id>/<int:powtoon_id>', views.powtoon_delete, name='powtoon_delete'),
    path('powtoon/my/<int:user_id>', views.powtoon_owned_by_a_user, name='powtoon_owned_by_a_user'),
    path('powtoon/shared_with_me/<int:user_id>', views.powtoon_shared_to_a_user, name='powtoon_shared_to_a_user'),
    path('powtoon/share', views.powtoon_share, name='powtoon_share')
]