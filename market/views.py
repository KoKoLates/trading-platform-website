from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item

# Create your views here.
def market_index(request):
    return render(request, 'mk_index.html', {'items': Item.objects.all()})

@login_required(login_url='market_index')
def user_interface(request):
    """"""
    if request.method in ('GET'):
        user = request.user.username
    return render(request, 'mk_user.html', {'items': Item.objects.filter(user=user)})


def create(request):
    if request.method in ('POST'):
        item = Item()
        item.user = request.user.username
        item.name = request.POST.get('name')
        item.price = request.POST.get('price')
        item.quantity = request.POST.get('quantity')
        item.category = request.POST.get('category')
        item.transaction_type = request.POST.get('transaction_type')
        item.transaction_location = request.POST.get('transaction_location', '')
        item.condition = request.POST.get('condition')
        item.image = request.FILES.get('image')
        item.save()

    return redirect('user')
    
def create_interface(request):
    return render(request, 'mk_create.html')
