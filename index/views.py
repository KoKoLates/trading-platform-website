from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import Campaign, Register

# Create your views here.
def index(request):
    return render(request, 'index.html', 
        {'campaigns': Campaign.objects.all(), 
         'registers': [register.campaign for register in \
                       Register.objects.filter(user=request.user.username)]
        })

def market_index(request):
    return render(request, 'mk_index.html')

def create_campaign(request):
    if request.method in ('POST'):
        campaign = Campaign()
        campaign.name = request.POST.get('name')
        campaign.date = request.POST.get('date')
        campaign.time = request.POST.get('time')
        campaign.location = request.POST.get('location')
        campaign.description = request.POST.get('description')
        campaign.announcer = request.user.username
        campaign.register_num = 0
        campaign.save()

    return redirect('index')

def delete_campaign(request, idx):
    if request.method in ('GET'):
        campaign = Campaign.objects.filter(idx=idx)
        campaign.delete()
        register = Register.objects.filter(campaign=idx)
        register.delete()
    return redirect('index')

@login_required(login_url='index')
def register_campaign(request, idx):
    if request.method in ('GET'):
        register = Register()
        register.user = request.user.username
        register.campaign = idx
        register.save()

        campaign = Campaign.objects.get(idx=idx)
        campaign.register_num += 1
        campaign.save()
    return redirect('index')

def cancel_campaign(request, idx):
    if request.method in ('GET'):
        register = Register.objects.filter(campaign=idx, user=request.user.username)
        register.delete()

        campaign = Campaign.objects.get(idx=idx)
        campaign.register_num -= 1
        campaign.save()
    
    return redirect('index')
