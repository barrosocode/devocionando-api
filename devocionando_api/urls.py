"""
URL configuration for devocionando_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

# Imports
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.api import viewsets as apiviewsets

# Route
route = routers.DefaultRouter()

# Rotas registradas
route.register(r'categories', apiviewsets.CategoryViewSet, basename='Categories')
route.register(r'churches', apiviewsets.ChurchViewSet, basename='Churches')
route.register(r'jobs', apiviewsets.JobViewSet, basename='Jobs')
route.register(r'roles', apiviewsets.RoleViewSet, basename='Roles')
route.register(r'ChurchRoles', apiviewsets.ChurchRoleViewSet, basename='ChurchRoles')
route.register(r'references', apiviewsets.ReferenceViewSet, basename='References')
route.register(r'author', apiviewsets.AuthorViewSet, basename='Authors  ')
route.register(r'articles', apiviewsets.ArticleViewSet, basename='Articles')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls))
]
