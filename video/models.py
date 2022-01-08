from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelState

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=50)
    slug = models.SlugField()
    created = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title