"""drf_test URL Configuration

The `urlpatterns` list routes URLs to example_views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function example_views
    1. Add an import:  from my_app import example_views
    2. Add a URL to urlpatterns:  path('', example_views.home, name='home')
Class-based example_views
    1. Add an import:  from other_app.example_views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.serializers import HyperlinkedModelSerializer
from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('snippets.urls')),
]
