from django.db import models
#from bloodbank.recipient import user
from datetime import datetime

class Plea(models.Model):
    '''This table will store all the pleas for blood.'''
    text = models.TextField()
    user = models.ForeignKey('recipient.User')
    date = models.DateTimeField(default = datetime.now())
    bloodGroup = models.ForeignKey('recipient.BloodGroup')
    location = models.ForeignKey('recipient.Locality')
    hospital = models.TextField() #Add a list of hospitals that are allowed to collect blood

class Response(models.Model):
    '''This table maps out who replied to a donation call.'''
    user = models.ForeignKey('recipient.User')
    text = models.TextField()
    eta = models.TextField()
    
