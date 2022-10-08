from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(request):
    products = Product.objects.all()
    n = len(products)
    nSlides = n//4 + ceil((n/2) - (n//4))

    # params = {'no_of_slides': nSlides, 'range' : (1, nSlides), 'product': products}
    allProds = [[products, range(3, nSlides), nSlides],
              [products, range(3, nSlides), nSlides]]
    params = {'allProds' : allProds} 
    return render(request, 'shop/index.html', params)

def about(request):
    # return HttpResponse("we are at about page")
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("we are at contact page")
    # return render(request, 'shop/index.html')

def tracker(request):
    return HttpResponse("we are tracker page")
    # return render(request, 'shop/index.html')

def search(request):
    return HttpResponse("we are at search page")
    # return render(request, 'shop/index.html')

def productview(request):
    return HttpResponse("we are at product view")
    # return render(request, 'shop/index.html')

def checkout(request):
    return HttpResponse("we are at checkout page")
    # return render(request, 'shop/index.html')


