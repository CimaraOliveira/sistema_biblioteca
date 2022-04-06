"""biblioteca_livros URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from livro.service_livro import listarLivro

router = routers.DefaultRouter()
router.register(r'livro', listarLivro)

#http://127.0.0.1:8000/api/ caminho da api

urlpatterns = [  
    path('admin/', admin.site.urls),
    path('', include('livro.urls')),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
