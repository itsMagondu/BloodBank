from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.mail import EmailMessage
from django.conf import settings

from apps.appadmin.models import WebsiteEmail

@login_required
def email_submit(request):
    #In future move this to admin                                                                                                               
    param = {}
    param['username'] = request.user
    param['media_url'] = settings.MEDIA_URL
    param['base_url'] = settings.BASE_URL

    if request.method == "POST":
       name = request.POST.get('name')
       email = request.POST.get('email')
       message = request.POST.get('message')

       #Store the email somewhere and forward it to the admin                                                                                   
       w = WebsiteEmail(sender = name,email = email,message=message)
       w.save()

       admins = settings.ADMINS
       subject = "Email from Website"

       #Use mail admins instead in future                                                                                                       
       for a in admins:
           to = [str(a[1])]
           EmailMessage(subject, message, to=to, from_email=email).send()

       param['success'] = "Your email was successfully sent"

    return render_to_response('biz/contact.html', param, context_instance=RequestContext(request))

