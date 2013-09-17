"""Here we have all user data. These people will send out requests for blood and will also be potential donors themselves"""
from django.db import models
from datetime import datetime

class BloodGroup(models.Model):
    '''stores the various blood group details'''
    name = models.TextField()
    rhesus = models.BooleanField()

class Locality(models.Model):
    '''This table will map out the various blood banks where transfusion is allowed'''
    name = models.TextField()
    center = models.TextField()

class User(models.Model):
    """Each user will provide this details so that they can get informed once a donation is needed"""
    
    bloodGroup = models.ForeignKey('BloodGroup')
    location = models.ForeignKey('Locality')
    firstname = models.TextField()
    lastname = models.TextField(null = True)
    othername = models.TextField(null = True)
    gender = models.TextField(null = True)
    DOB = models.TextField(null = True)
    cellphone  = models.TextField(null=False)
    joined = models.DateTimeField(default = datetime.now())


class UserIllness(models.Model):
    '''This table stores a list of all diseases a user has contracted that can make their blood untransfusable'''
    bloodGroup = models.ForeignKey('User')
    location = models.ForeignKey('Disease')

class Disease(models.Model):
    '''stores the various diseases that can cause blood to be rejected'''
    name = models.TextField()
    center = models.TextField()
