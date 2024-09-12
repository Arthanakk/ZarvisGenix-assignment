from django.shortcuts import render,redirect
from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.http import HttpResponse
# Create your views here.

def register(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password']
        if password == cpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, "email taken")
                return redirect('register')
            else:
                user = User.objects.create_user(
                                                email=email,
                                                password=password)
                user.save()
                print("user registered")

        else:
            messages.info(request, "password not match")
            return redirect('register')
        return redirect('/')
    else:
        return render(request,'register.html')
def login(request):
    if request.method=='POST':
        email=request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('register')
        else:
            messages.info(request, 'invalid login')
    else:
        return render(request,'index.html')