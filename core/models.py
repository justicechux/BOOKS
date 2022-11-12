from distutils.command.upload import upload
from email.policy import default
from time import timezone
from django.db import models
from django.utils import timezone

# Create your models here.


class author(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length = 100)
    content = models.TextField()
    author = models.ManyToManyField(author)
    published_date = models.DateTimeField(default=timezone.now)
    cover_image = models.ImageField(default="defult.png", upload_to="profile_pics")

    def __str__(self):
        return self.title