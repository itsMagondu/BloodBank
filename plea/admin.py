from rbd.plea.models import *
from rbd.recipient.models import *
from django.contrib import admin

class PleaAdmin(admin.ModelAdmin):
    list_display = ('text','user','date','bloodGroup','location','hospital')

class ResponseAdmin(admin.ModelAdmin):
    list_display = ('user','text','eta')

admin.site.register(Plea, PleaAdmin)
admin.site.register(Response, ResponseAdmin)
