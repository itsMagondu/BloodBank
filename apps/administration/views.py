from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.shortcuts import *
from django.http import *

from apps.administration.models import SignUp

@login_required
def login(request):
	return render_to_response('signin.html')

@login_required
def home(request):
	param = {}
	param['username'] = request.user
	param['media'] = settings.MEDIA_URL
	return render_to_response('biz/index.html', param)

@login_required
#def register(request):
#	param = {}
#	param['username'] = request.user
#	return render_to_response('register.html', param)
def register(request):
    '''Render the regisration form on the interface'''
    count = 0
    def errorHandle(error):
        form = SignUp()
        return render_to_response('register.html', {'error' : error,'form' : form,})

    if request.method == 'POST':
        form = GetCSVFile(request.POST, request.FILES) #Get the CSV file from the form
        if form.is_valid():
            message = request.POST['message']
            error = "welcome to RBD!"
            return render_to_response('register.html', {'error': error,'form' : form,})
        else:
            form = GetCSVFile()
            error = "Something in the form is invalid"
            return render_to_response('register.html', {'error' : error,'form' : form,})
    else:
        form = SignUp()
    return render_to_response('register.html', {'form': form})
