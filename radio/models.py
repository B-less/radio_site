from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

class RadioStation(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    stream_url = models.URLField()
    image = models.ImageField(upload_to='stations/', blank=True, null=True)
    current_listeners = models.PositiveIntegerField(default=0)
    monthly_plays = models.PositiveIntegerField(default=0)
    
    # Ensure these fields are defined
    image = models.ImageField(upload_to='stations/', null=True, blank=True)
    
    CATEGORY_CHOICES = [
        ('music', 'Music'),
        ('news', 'News'),
        ('sports', 'Sports'),
        ('talk', 'Talk Radio'),
    ]
    category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Station(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
   
    stream_url = models.URLField()  # This is the URL to the streaming audio

    def __str__(self):
        return self.name


