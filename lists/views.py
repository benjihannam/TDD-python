from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

ITEM_TEXT = 'item_text'


def home_page(request):
    return render(request, 'home.html')


def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    list_ = List.objects.create()
    Item.objects.create(text=request.POST[ITEM_TEXT], list=list_)
    return redirect('/lists/the-only-list-in-the-world/')