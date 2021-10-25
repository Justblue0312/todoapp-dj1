from django.urls import path
from . import views

urlpatterns = [

    path('', views.ListWishes, name='list'),

    path('add', views.AddWishlist, name='add'),
    path('edit/<int:id>', views.editWishlist, name='edit'),
    path('delete/<int:id>', views.deleteWishlist, name='delete'),

]
