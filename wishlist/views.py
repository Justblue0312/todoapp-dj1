from django.shortcuts import render, redirect
from .models import *
from .forms import AddWishlistForm
import datetime
from .utils import SearchWishlist


def index(request):
    return render(request, 'index.html')


def ListWishes(request):

    wishlist, search_query = SearchWishlist(request)

    context = {'wishlist': wishlist, 'search_query': search_query}
    return render(request, 'list.html', context)


def AddWishlist(request):
    form = AddWishlistForm
    if request.method == 'POST':
        form = AddWishlistForm(request.POST)
        if form.is_valid():
            wish = form.save(commit=True)
            wish.save()
            return redirect('list')

    context = {'form': form}
    return render(request, 'wishlist_form.html', context)


def editWishlist(request, id):
    obj = Wishlist.objects.get(id=id)
    form = AddWishlistForm(instance=obj)
    if request.method == 'POST':
        form = AddWishlistForm(request.POST, instance=obj)
        if form.is_valid():
            update_at = datetime.datetime.now()
            obj.created_at = update_at
            form.save()
            return redirect('list')
    context = {'form': form}
    return render(request, 'wishlist_form.html', context)


def deleteWishlist(request, id):
    obj = Wishlist.objects.get(id=id)

    if request.method == 'POST':
        obj.delete()
        return redirect('list')

    context = {'obj': obj}
    return render(request, 'detele_template.html', context)
