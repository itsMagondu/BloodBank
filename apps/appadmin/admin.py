from django.contrib import admin
from apps.appadmin.models import WebsiteEmail

# Register your models here.
class  WebEmailAdmin(admin.ModelAdmin):
    list_display = ('sender','email','message','received')

admin.site.register(WebsiteEmail, WebEmailAdmin)

