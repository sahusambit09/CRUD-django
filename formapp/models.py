from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    image = models.ImageField(upload_to='profile/', null=True)
    document = models.FileField(upload_to='docs/', null=True)
