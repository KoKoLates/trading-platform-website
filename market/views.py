from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Item, Love, Comment

# global variable setup here for flag
user_item_flag, love_item_flag = False, False

preview_index = None
category_type = None
category_list = [
    '衣物服飾', '鞋子', '電子設備', '其他物件'
]

# Create your views here.
def market_index(request):
    global preview_index
    return render(request, 'mk_index.html', {
        'items': Item.objects.all() if not category_type \
            else Item.objects.filter(category=category_type),
        'category': category_type,
        'previews': preview_index,
        'love_items': [love.item for love in \
                       Love.objects.filter(user=request.user.username)],
        'comments': Comment.objects.filter(item_idx=preview_index)
    })

@login_required(login_url='market_index')
def user_interface(request):
    global user_item_flag, love_item_flag, category_type
    if request.method in ('GET'):
        user = request.user.username

    if user_item_flag:
        return  render(request, 'mk_user.html', {
            'items': Item.objects.filter(user=user, category=category_type) \
                if category_type else Item.objects.filter(user=user),
            'category': category_type,
            'previews': preview_index,
            'user_check': 'check',
            'comments': Comment.objects.filter(item_idx=preview_index),
            'love_items': [love.item for love in \
                           Love.objects.filter(user=request.user.username)],
        })
    elif love_item_flag:
        love_item = [item.item for item in Love.objects.filter(user=user)]
        return  render(request, 'mk_user.html', {
            'items': Item.objects.filter(user=user, category=category_type, idx__in=love_item) \
                if category_type else Item.objects.filter(user=user, idx__in=love_item),
            'category': category_type,
            'previews': preview_index,
            'love_check': 'check',
            'comments': Comment.objects.filter(item_idx=preview_index),
            'love_items': [love.item for love in \
                           Love.objects.filter(user=request.user.username)],
        })
    else:
        return redirect('market_index')
    
def search_interface(request):
    keyword = request.GET.get('keyword')
    print(keyword)
    return render(request, 'mk_search.html')

def category(request, option):
    global category_type
    global preview_index
    preview_index = None
    if request.method in ('GET'):
        category_type = option if option in category_list else None

    return redirect('user_interface' if user_item_flag or love_item_flag else 'market_index')

@login_required(login_url='market_index')
def create(request):
    global preview_index
    preview_index = None
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

@login_required(login_url='market_index')
def create_interface(request):
    global preview_index
    preview_index = None
    return render(request, 'mk_create.html', {
        'items': Item.objects.filter(user=request.user.username),
        'user_check': 'check',
        'love_items': [love.item for love in \
                       Love.objects.filter(user=request.user.username)],
    })

@login_required(login_url='market_index')
def love_item(request, idx):
    global preview_index
    preview_index = None
    if request.method in ('GET'):
        user = request.user.username
        Love.objects.filter(user=user, item=idx).delete() \
            if Love.objects.filter(user=user, item=idx).exists() \
                else Love(user=user, item=idx).save()

    return redirect('market_index')

@login_required(login_url='market_index')
def remove_item(request, idx):
    global preview_index
    preview_index = None
    if request.method in ('GET'):
        Item.objects.filter(user=request.user.username, idx=idx).delete()
        Love.objects.filter(user=request.user.username, item=idx).delete()
        Comment.objects.filter(item_idx=idx).delete()

    return redirect('user_interface')

def comment(request, idx):
    if request.method in ('POST'):
        Comment(
            item_idx = idx,
            username = request.user.username,
            contents = request.POST.get('comment')
        ).save()
    
    return redirect('user_interface' if user_item_flag or love_item_flag else 'market_index')

def preview_item(request, idx):
    global preview_index
    if request.method in ('GET'):
        preview_index = int(idx)

    return redirect('user_interface' if user_item_flag or love_item_flag else 'market_index')

## function for changing btn status
def user_btn(request):
    global preview_index
    preview_index = None ## clean the preview block

    global user_item_flag, love_item_flag
    if love_item_flag:
        love_item_flag = False
    user_item_flag = not user_item_flag
    return redirect('user_interface')

def love_btn(request):
    global preview_index
    preview_index = None ## clean the preview block

    global user_item_flag, love_item_flag
    user_item_flag = not user_item_flag if user_item_flag else user_item_flag
    love_item_flag = not love_item_flag
    return redirect('user_interface')
