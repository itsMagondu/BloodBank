from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from django.http import *

@login_required
def login(request):
	return render_to_response('signin.html')


@login_required
def home(request):
	param = {}
	param['username'] = request.user
	return render_to_response('home.html', param)

@login_required
def register(request):
	param = {}
	param['username'] = request.user
	return render_to_response('register.html', param)

def upload_file(request):
    '''Gets a file that is to be uploaded using a post request and sends them a survey invitation message'''
    count = 0
    def errorHandle(error):
        form = GetCSVFile()
        return render_to_response('kssha/upload.html', {'error' : error,'form' : form,})

    if request.method == 'POST':
        form = GetCSVFile(request.POST, request.FILES) #Get the CSV file from the form
        if form.is_valid():
            csvfile = request.FILES['file']
            message = request.POST['message']
            
            for line in csvfile:
                line = line.split(',')
                name = str(line[0])
                number = int(str(line[1]))
                sendMessage(number,name,message)
            
            error = "Messages have been sent"
            return render_to_response('kssha/upload.html', {'error': error,'form' : form,})
        else:
            form = GetCSVFile()
            error = "Something in the form is invalid"
            return render_to_response('kssha/upload.html', {'error' : error,'form' : form,})
    else:
        form = GetCSVFile()
    return render_to_response('kssha/upload.html', {'form': form})
