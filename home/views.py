from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth import login
from django.shortcuts import redirect


# Create your views here.
# Create your views here.
from django.http import HttpResponse
 
def index(request):
    if request.user.is_anonymous:
	    return redirect('/login')
    else:
	    return render(request,'index.html')

def loginuser(request):
    if(request.method == 'POST'):
	    username1 = request.POST.get('username')
	    password1 = request.POST.get('password')
	    user = authenticate(username=username1, password=password1)
	    if user is not None:
		    login(request,user)
		    return redirect('/')
	    else:
		    return render(request,'login.html')

    return render(request,'login.html')
	
def logoutuser(request):
    logout(request)
    return redirect('/login')