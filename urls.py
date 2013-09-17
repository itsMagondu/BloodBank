from django.conf.urls import patterns, include, url

#Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'home/$', 'bloodbank.admin.views.home', name='home'),
    url(r'register/$', 'rbd.admin.views.register', name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', 
    {'template_name': 'login.html'}),
    url(r'^$', 'bloodbank.admin.views.home', name='home'),
    #url(r'^login/', 'bloodbank.admin.views.login'),
    # url(r'^bloodbank/', include('bloodbank.foo.urls')),

     #Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

     #Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
