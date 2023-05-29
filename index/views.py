from django.shortcuts import render
from django.contrib import auth
from .models import Campaign

# Create your views here.
def index(request):

    # testing user login
    # user = auth.authenticate(username='koko', password='123')
    # auth.login(request, user)

    return render(request, 'index.html', {'campaigns': Campaign.objects.all()})


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

    return render(request, 'index.html', {'campaigns': Campaign.objects.all()})

def market_index(request):
    return render(request, 'mk_index.html')
