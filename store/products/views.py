from django.shortcuts import render
from products.models import *


def index(request):
    context = {
        'title': 'Test Title',
            }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
