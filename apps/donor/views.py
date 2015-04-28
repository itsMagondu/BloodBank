from django.contrib.auth.decorators import login_required
from django.conf import settings

from django.shortcuts import render_to_response

from apps.donor.models import Register

@login_required
def login(request):
    return render_to_response('signin.html')

@login_required
def home(request):
    param = {}
    param['username'] = request.user
    param['media_url'] = settings.MEDIA_URL
    param['base_url'] = settings.BASE_URL
    return render_to_response('biz/index.html', param)

def about(request):
    param = {}
    param['username'] = request.user
    param['media_url'] = settings.MEDIA_URL
    param['base_url'] = settings.BASE_URL
    return render_to_response('biz/about.html', param)

@login_required
def register(request):
    '''Render the regisration form on the interface'''
    param = {}
    param['username'] = request.user
    param['media_url'] = settings.MEDIA_URL
    param['base_url'] = settings.BASE_URL

    def errorHandle(error):
        form = Register()

        param = {}
        param['username'] = request.user
        param['media_url'] = settings.MEDIA_URL
        param['base_url'] = settings.BASE_URL
        param['error'] = error
        param['form'] = form
        return render_to_response('biz/register.html', param)

    if request.method == 'POST':
        form = Register(request.POST)
        

        if form.is_valid():
            message = request.POST['message']
            error = "Welcome to Donor Link! Please check your email"
            param['form'] = form
            param['error'] = error
            param['message'] = message

            #Send a user a welcome email. If you can, also send an sms
            return render_to_response('register.html', param)
        else:
            form = Register()
            error = "Something in the form is invalid"

            param['form'] = form
            param['error'] = error

            return render_to_response('biz/register.html', param)
    else:
        form = Register()
        param['form'] = form
        
    return render_to_response('biz/register.html', param)


def register_user():
    if request.method == 'POST':
        """Create user"""
        firstname = request.POST.get("firstname",None)
        lastname = request.POST.get("lastname",None)
        gender = request.POST.get("gender",None)
        dob = request.POST.get("dob",None)
        phone = request.POST.get("phone",None)
        email = request.POST.get("email",None)
        bloodgroup = request.POST.get("bloodgroup",None)

        u = User()
        u.firstname = firstname
        u.lastname = lastname
        u.gender = gender
        u.date_of_birth = dob
        u.phone = phone
        u.email = email
        u.bloodgroup = bloodgroup
        u.save()

        param = {}
        param['user'] = u
        param['media_url'] = settings.MEDIA_URL
        param['base_url'] = settings.BASE_URL
        
        param['success'] = "Registration successful. Welcome" 
        
        return render_to_response('biz/register.html', param)
        
    else:
        param = {}
        param['username'] = request.user
        param['media_url'] = settings.MEDIA_URL
        param['base_url'] = settings.BASE_URL
        
        param['counties'] = Register.Counties
        param['gender'] = Register.Gender
        param['bloodgroup'] = Register.Bloodgroup 
        
        return render_to_response('biz/register.html', param)
        
