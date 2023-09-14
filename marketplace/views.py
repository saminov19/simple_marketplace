from django.shortcuts import render
from .models import Product, Category, Tag


def product_search(request):
    query = request.GET.get('query', '')
    category_id = request.GET.get('category', '')
    tag_ids = request.GET.getlist('tag', '')

    products = Product.objects.filter(description__icontains=query)

    if category_id:
        products = products.filter(category=category_id)

    if tag_ids:
        products = products.filter(tags__in=tag_ids).distinct()

    categories = Category.objects.all()
    tags = Tag.objects.all()

    return render(request, 'marketplace/product_list.html', {
        'products': products,
        'categories': categories,
        'tags': tags,
    })
