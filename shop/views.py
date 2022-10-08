from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'shop/index.html')

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


