from django.conf.urls import patterns, include, url

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #MEDIA PATH                                                                                                                                
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

    url(r'home/$', 'apps.administration.views.home', name='home'),
    url(r'about/$', 'apps.administration.views.about', name='about'),
    url(r'register/$', 'apps.administration.views.register', name='home'),

    url(r'^login/$', 'django.contrib.auth.views.login', 
    {'template_name': 'login.html'}),

    url(r'^$', 'apps.administration.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
