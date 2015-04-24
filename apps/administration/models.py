from django.db import models
from django import forms
from datetime import datetime
from django.contrib.auth.models import User

class UserDetail(models.Model):
    """Additional user information will be stored here as on top of what django already handles"""

    bloodgroup = models.IntegerField()

    userCounty = models.TextField()
    
    joined = models.DateTimeField(default = datetime.now())

    user = models.ForeignKey(User, unique=True)

class Register(forms.Form):
    '''This will be used to select the file from the local machine'''
    
    Gender = (
        ('1', 'Male'),
        ('2', 'Female'),
        )
    ''' Example from See more at: http://ilian.i-n-i.org/django-forms-choicefield-with-dynamic-values/#sthash.DbIACTyM.dpuf'''
    
    '''Obtained from http://changamkamkenya.blogspot.com/2010/09/complete-list-of-47-new-counties-of.html'''
    Counties = (
        ('Kiambu','Kiambu'),
        ('Mombasa','Mombasa'),
        ('Kwale','Kwale'),
        ('Kilifi','Kilifi'),
        ('Tana River','Tana River'),
        ('Lamu','Lamu'),
        ('Taita Taveta','Taita Taveta'),
        ('Garissa','Garissa'),
        ('Wajir','Wajir'),
        ('Mandera','Mandera'),
        ('Marsabit','Marsabit'),
        ('Isiolo','Isiolo'),
        ('Meru','Meru'),
        ('Tharaka Nithi','Tharaka Nithi.'),
        ('Embu','Embu'),
        ('Kitui','Kitui'),
        ('Machakos','Machakos'),
        ('Makueni','Makueni'),
        ('Nyandarua','Nyandarua'),
        ('Nyeri','Nyeri'),
        ('Kirinyaga','Kirinyaga'),
        ("Murang'a","Murang'a"),
        ('Turkana','Turkana'),
        ('West Pokot','West Pokot'),
        ('Samburu','Samburu'),
        ('Trans Nzoia','Trans Nzoia'),
        ('Uasin Gishu','Uasin Gishu'),
        ('Elgeyo/Marakwet','Elgeyo/Marakwet'),
        ('Nandi','Nandi'),
        ('Baringo','Baringo'),
        ('Laikipia','Laikipia'),
        ('Nakuru','Nakuru'),
        ('Narok','Narok'),
        ('Kajiado','Kajiado'),
        ('Kericho','Kericho'),
        ('Bomet','Bomet'),
        ('Kakamega','Kakamega'),
        ('Vihiga','Vihiga'),
        ("Bung'oma","Bung'oma"),
        ('Busia','Busia'),
        ('Siaya','Siaya'),
        ('Kisumu','Homa Bay'),
        ('Homa Bay','Homa Bay'),
        ('Migori','Migori'),
        ('Kisii','Kisii'),
        ('Nyamira','Nyamira'),
        ('Nairobi','Nairobi'),
        )
    
    surname = forms.CharField(max_length=100)
    other_names = forms.CharField(max_length=100)
    gender = forms.ChoiceField(choices=Gender)
    Date_Of_Birth = forms.CharField(max_length=100)
    email_Address= forms.EmailField()
    mobile_Number = forms.CharField(max_length=100)
    bloodgroup = forms.CharField(max_length=100)
    county = forms.ChoiceField(choices=Counties)

