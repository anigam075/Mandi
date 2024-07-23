from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('about', about, name='about'),
    path('blog', blog, name='blog'),
    path('blog_single', blog_single, name='blog_single'),
    path('cart', cart, name='cart'),
    path('product_single', product_single, name='product_single'),
    path('contact', contact, name='contact'),
    path('checkout', checkout, name='checkout'),
    path('shop', shop, name='shop'),
    path('wishlist', wishlist, name='wishlist'),
]
