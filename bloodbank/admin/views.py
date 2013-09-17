from django.contrib.auth.decorators import login_required
from django.shortcuts import *
from django.http import *

@login_required
def home(request):
	param = {}
	param['username'] = request.user
	return render_to_response('home.html', param)
