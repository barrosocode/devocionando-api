from rest_framework import serializers
from api import models

# Category Serializer
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

# Church Serializer
class ChurchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Church
        fields = '__all__'

# Job Serializer
class JobsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Job
        fields = '__all__'

# Role Serializer
class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = '__all__'

# ChurchRole Serializer
class ChurchesRolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChurchRole
        fields = '__all__'

# Reference Serializer
class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Reference
        fields = '__all__'

# Author Serializer
class AuthorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Author
        fields = '__all__'

# Article Serializer
class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Article
        fields = '__all__'
