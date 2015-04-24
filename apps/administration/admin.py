from apps.administration.models import *
from django.contrib import admin

class  UserDetailAdmin(admin.ModelAdmin):
    list_display = ('bloodgroup','userCounty','joined','user')

#class RegisterAdmin(admin.ModelAdmin):
#    list_display = ('name','message')

admin.site.register(UserDetail, UserDetailAdmin)
#admin.site.register(Register, RegisterAdmin)
