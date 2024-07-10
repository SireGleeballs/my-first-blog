from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
class Form(models.Model):
    name = models.CharField(max_length=200)
    address_L1 = models.CharField(max_length=200)
    address_L2 = models.CharField(max_length=200)
    postcode = models.CharField(max_length=200)

    def __str__(self):
        return self.name
