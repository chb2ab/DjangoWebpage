from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
from django.http import HttpResponse


from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
	
def index(request):
    return render(request,'registration/login.html');


def success(request):
	return render(request,'registration/success.html')

def login(request):

    user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

# At this point, user is a User object that has already been saved
# to the database. You can continue to change its attributes
# if you want to change other fields.
    user.last_name = 'Lennon'
    user.save()
    username = request.POST.get('username',False)
    password = request.POST.get('password',False)
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return render(request,'success.html')
        else:
        	return render(request,'fail.html')
            
    else:
    	return render(request,'fail.html')
