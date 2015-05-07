from django.db import models

# Create your models here.

class WebsiteEmail(models.Model):
    sender = models.CharField(max_length=100,default="")
    email = models.EmailField(default="")
    message = models.CharField(max_length=100,default="")
    received = models.DateTimeField(auto_now_add=True)
  
    def __unicode__(self):
        return self.email
