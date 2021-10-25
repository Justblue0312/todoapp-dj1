from .models import Wishlist
from django.db.models import Q


def SearchWishlist(request):
    search_query = ''

    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    wishlist = Wishlist.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(priority__icontains=search_query)
    )

    return wishlist, search_query
