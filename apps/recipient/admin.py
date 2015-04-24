from apps.recipient.models import *
from django.contrib import admin

class  BloodGroupAdmin(admin.ModelAdmin):
    list_display = ('name','rhesus')

class  LocalityAdmin(admin.ModelAdmin):
    list_display = ('name','center')

class  UserAdmin(admin.ModelAdmin):
    list_display = ('bloodGroup','location','firstname','lastname','gender','DOB')

class UserIllnessAdmin(admin.ModelAdmin):
    list_display = ('user','disease')


admin.site.register(BloodGroup, BloodGroupAdmin)
admin.site.register(Locality, LocalityAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(UserIllness , UserIllnessAdmin)
