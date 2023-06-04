from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item

# global variable setup here for flag
user_item_flag, love_item_flag = False, False

category_type = None
category_list = [
    '衣物服飾', '鞋子', '電子設備', '其他物件'
]

# Create your views here.
def market_index(request):
    return render(request, 'mk_index.html', {
        'items': Item.objects.all() if not category_type else Item.objects.filter(category=category_type),
        'category': category_type
    })

def category(request, option):
    global category_type
    if request.method in ('GET'):
        category_type = option if option in category_list else None

    return redirect('user_interface' if user_item_flag else 'market_index')

@login_required(login_url='market_index')
def user_interface(request):
    """"""
    global user_item_flag, category_type
    if request.method in ('GET'):
        user = request.user.username

    return  render(request, 'mk_user.html', {
        'items': Item.objects.filter(user=user), 
        'category': category_type, 
        'user_check': 'Check'
    }) if user_item_flag else redirect('market_index')
    
def user_btn(request):
    global user_item_flag
    user_item_flag = not user_item_flag
    return redirect('user_interface')

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

    return redirect('user_interface')
    
def create_interface(request):
    return render(request, 'mk_create.html')
