from django.db import models
 
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.JSONField()
    phone = models.CharField(max_length=100)
    website = models.CharField(max_length=100)
    company = models.JSONField()

class Post(models.Model):
    userId = models.IntegerField()
    id = models.IntegerField(primary_key=True)
    title = models.TextField()
    body = models.TextField()
