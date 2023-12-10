from django.shortcuts import render, get_object_or_404
from .models import Product, Category
from django.views.generic import TemplateView, DetailView, ListView


def product_list(request):
    category = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products, 'category': category})


class About:
    pass


class Contact:
    pass


class Single(DetailView):
    template_name = 'single-product.html'
    model = Product


class Products(TemplateView):
    template_name = 'products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_id = kwargs['category_id']
        post = get_object_or_404(Category, id=category_id)
        posty = Product.objects.filter(category=post)
        cater = Category.objects.all()
        context['post'] = post
        context['posty'] = posty
        context['cater'] = cater
        return context
