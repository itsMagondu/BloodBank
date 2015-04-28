from apps.donor.models import *
from django.contrib import admin

class  UserProfileAdmin(admin.ModelAdmin):
    list_display = ('bloodgroup','county','joined','user')

admin.site.register(UserProfile, UserProfileAdmin)
