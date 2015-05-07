from django.conf.urls import patterns, include, url

from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    #MEDIA PATH                                                                                                                                
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT }),

    url(r'home/$', 'apps.donor.views.home', name='home'),
    url(r'about/$', 'apps.donor.views.about', name='about'),
    url(r'register/$', 'apps.donor.views.register', name='register'),
    url(r'gallery/$', 'apps.donor.views.gallery', name='gallery'),
    url(r'contact/$', 'apps.donor.views.contact', name='contact'),
    url(r'email/submit/$', 'apps.donor.views.email_submit', name='submit_email'),
    url(r'reg/$', 'apps.donor.views.register_user', name='reg'),

    url(r'^login/$', 'django.contrib.auth.views.login', 
    {'template_name': 'login.html'}),

    url(r'^$', 'apps.donor.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
