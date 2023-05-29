from django.shortcuts import render

# Create your views here.
def market_index(request):
    return render(request, 'mk_index.html')


