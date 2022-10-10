from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()

    allProds = []
    CatProd = Product.objects.values('category', 'id')
    cats = {item['category'] for item in CatProd}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/2) - (n//4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides': nSlides, 'range' : (1, nSlides), 'product': products}
    # allProds = [[products, range(3, nSlides), nSlides],
    #           [products, range(3, nSlides), nSlides]]
    params = {'allProds' : allProds} 
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def search(request):
    return render(request, 'shop/search.html')

def productview(request, myid):
    # fetch product using id

    product = Product.objects.filter(id=myid)
    print(product)
    params = {'product': product}
    return render(request, 'shop/prodview.html', params)

def checkout(request):
    return render(request, 'shop/checkout.html')


