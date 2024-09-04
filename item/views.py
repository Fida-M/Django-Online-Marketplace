from django.shortcuts import render, get_object_or_404
from .models import Category, Item

# Create your views here.
# def index(request):
#     items = Item.objects.filter(is_sold=False)[0:6]
#     categories = Category.objects.all
#     return render(request, 'core/index.html', {
#         'categories': categories,
#         'items': items,
#     })


def detail (request, pk):
    item = get_object_or_404(Item, pk=pk)
    realted_items =Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]

    return render(request, 'item/detail.html', {
        'item': item ,
        'realted_items': realted_items
        })
