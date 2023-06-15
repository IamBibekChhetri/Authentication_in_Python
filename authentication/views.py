
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib import messages
from authentication.models import CustomUser
from django.contrib.auth import authenticate,login,logout


# Create your views here.
def home(request):
    return render(request,"authentication/index.html")

def signup(request):
    if request.method == 'POST':
        username=request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=CustomUser.objects.create_user(username=username,password=password,email=email)
        user.save()
        # print("Your Account has been created successfully!")
        messages.success(request,"Your Account has been created successfully")

        return redirect('/signin')

        
    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == 'POST':
       email = request.POST.get('email')
       password = request.POST.get('password')
       user = authenticate(request,email=email, password=password)
    #    print(user)
       if user is not None:
           login(request,user)
           messages.info(request,'You are now logged in!')
           return redirect("home")
       else:
           messages.error(request,'Invalid Credentials!')
           return redirect('home')

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request,"You have been log out successfully")
    return redirect('home')


def profile(request):

    return render(request,"authentication/profile.html")


def changePassword(request):

    return render(request,"authentication/changePassword.html")


def resetPassword(request):

    return render(request,"authentication/resetPassword.html")