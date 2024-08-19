from django.db import models
from django_resized import ResizedImageField



# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = ResizedImageField(size=[1000, 600], upload_to='media')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title