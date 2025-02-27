from rest_framework import viewsets
from api.api import serializers
from api import models

# Category Viewset
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.CategoriesSerializer
    queryset = models.Category.objects.all()

# Church Viewset
class ChurchViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChurchesSerializer
    queryset = models.Church.objects.all()

# Job Viewsets
class JobViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.JobsSerializer
    queryset = models.Job.objects.all()

# Role Viewsets
class RoleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RolesSerializer
    queryset = models.Role.objects.all()

# ChurchRole Viewsets
class ChurchRoleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ChurchesRolesSerializer
    queryset = models.Role.objects.all()

# Reference Viewset
class ReferenceViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ReferencesSerializer
    queryset = models.Reference.objects.all()

# Author Viewset
class AuthorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AuthorsSerializer
    queryset = models.Author.objects.all()

# Article Viewset
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ArticlesSerializer
    queryset = models.Article.objects.all()
