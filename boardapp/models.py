from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings

# Create your models here.

class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    images = models.ImageField(upload_to='', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    readtext = models.CharField(max_length=100, null=True, blank=True, default='a')
    goodtext = models.CharField(max_length=100, null=True, blank=True, default='a')
    
    def __str__(self):
        return self.title

