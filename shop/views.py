from django.shortcuts import render
from .models import Product
from math import ceil

# Create your views here.
from django.http import HttpResponse

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allprods = [[products,range(1,len(products)),nSlides],[products,range(1,len(products)),nSlides]]

    allprods = []
    catprods = Product.objects.values("category","id")
    cats = {item["category"] for item in catprods}

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n//4 + ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])
    
    

    params = {"allprods":allprods}
    return render(request, 'shop/harry.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productView(request):
    return render(request, 'shop/prodview.html')

def checkout(request):
    return render(request, 'shop/checkout.html')