from django.shortcuts import render, get_object_or_404
from .models import Product ,Category
from django.views.generic import TemplateView, DetailView, ListView


def product_list(request):
    category = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products,'category':category})


class About:
    pass


class Contact:
    pass


class Single(DetailView):
    template_name = 'single-product.html'
    model = Product


def product(request):
    return None
