from django.db import models
from uuid import uuid4

# Create your models here.

'''

Banco de dados Devocionando

#Article
ID (PK, not null, unique)
Author (FK)
Category (FK)
References (FK)
PostDate (not null, date)
Title (not null, varchar=30, default "sem título")
Resume (not null, varchar 500, default "sem resumo")
Text (not null, sem limite de tamanho)

#Category
ID (PK, not null, unique)
Name (not null, varchar=15, unique)

#Role
ID (PK, not null, unique)
Name (not null, varchar=15, unique)
Church (not null, varchar 30, unique)
Job (not null, varchar 30, unique)

#References
ID (PK, not null, unique)
Name (not null, varchar=100, unique)
Link (not null, varchar=100, unique)
Book (not null, varchar=100, unique)
BookAuthor (not null, varchar=100, unique)

#Author
ID (PK, not null, unique)
Role (FK)
Name (not null, varchar=100)
Birth (not null, date)
Email (not null, varchar=30, unique)
PhoneNumber (not null, varchar=15, unique)

'''

# Category
class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=15, null=False, unique=True)

# Church
class Church(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30, null=False, unique=True)

# Job
class Job(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=30, null=False, unique=True)

# Role
class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=15, null=False, unique=True)

# ChurchRole
class ChurchRole(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    church = models.ForeignKey(Church, on_delete=models.CASCADE)
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    name = models.ForeignKey(Role, on_delete=models.CASCADE)

# References
class Reference(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=100, null=False, unique=True)
    link = models.CharField(max_length=100, null=False, unique=True)
    book = models.CharField(max_length=100, null=False, unique=True)
    book_author = models.CharField(max_length=100, null=False, unique=True)

# Author
class Author(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    role = models.ForeignKey(ChurchRole, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, null=False, unique=True)
    birth = models.DateField(null=False)
    email = models.EmailField(null=False, max_length=30, unique=True)
    phone_number = models.CharField(max_length=15, null=False, unique=True)

# Article
class Article(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    references = models.ForeignKey(Reference, on_delete=models.CASCADE)
    post_date = models.DateField(null=False)
    title = models.CharField(max_length=30, null=False, default='Sem título')
    resume = models.CharField(max_length=500, null=False, default='Sem resumo')
    text = models.TextField(null=False)
