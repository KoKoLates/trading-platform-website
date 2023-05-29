from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from login.utils import mail_for_token_verification
from .models import Profile

import uuid

# Create your views here.
def login_interface(request):
    """ The view function of root login interface """
    return render(request, 'lg_logout.html') if request.user.is_authenticated \
        else render(request, 'lg_login.html')

def login_attempt(request):
    if request.method in ('POST'):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=username).first()

        if not user_obj:
            messages.success(request, 'User not found')
            return redirect('login_interface')
        
        profile_obj = Profile.objects.filter(user=user_obj).first()
        if not profile_obj or not profile_obj.verified:
            messages.success(request, 'Profile is not verified check your mail.')
            return redirect('login_interface')
        
        user = authenticate(username=username , password=password)
        if not user:
            messages.success(request, 'Wrong password.')
            return redirect('login_interface')
        
        login(request , user)
        return redirect('/')

    return render(request , 'lg_login.html')
        
def logout_attempt(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method in  ('POST'):
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            if User.objects.filter(username=username).first():
                messages.success(request, 'Username is taken.')
                return redirect('register')

            if User.objects.filter(email=email).first():
                messages.success(request, 'Email is taken.')
                return redirect('register')
            
            user_obj = User(username=username , email=email)
            user_obj.set_password(password)
            user_obj.save()
            auth_token = str(uuid.uuid4())
            profile_obj = Profile.objects.create(user=user_obj , token=auth_token)
            profile_obj.save()

            mail_for_token_verification(email, auth_token)
            return redirect('send_token')

        except Exception as exception:
            print(exception)
            
    return render(request , 'lg_register.html')

## password function
def send_token(request):
    return render(request, 'lg_token.html')

def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token=token).first()
        if profile_obj:
            if profile_obj.verified:
                messages.success(request, 'Your account is already verified.')
                return redirect('login')
            profile_obj.verified = True
            profile_obj.save()
            messages.success(request, 'Your account has been verified.')
            return redirect('login')
        else:
            return redirect('error')
    except Exception as exception:
        print(exception)
        redirect('/')

def error(request):
    return render(request, 'lg_error.html')

def forget_password(request):
    """ pass """

def change_password(request):
    """ pass """
