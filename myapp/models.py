from django.db import models

# Create your models here.

class Feed(models.Model):
  linkFile = models.CharField(max_length=200, unique=True)
  description = models.CharField(max_length = 200, blank=True, null=True)
  active = models.BooleanField(default=True)
  
  def __str__(self):
    return str(self.description)

class Link(models.Model):
  parentFeed = models.ForeignKey(Feed, on_delete=models.CASCADE)
  linkId = models.CharField(max_length=32)