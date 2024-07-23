from django.shortcuts import render, redirect

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog(request):
    return render(request, 'blog.html')

def blog_single(request):
    return render(request, 'blog-single.html')

def cart(request):
    return render(request, 'cart.html')

def product_single(request):
    return render(request, 'product-single.html')

def contact(request):
    return render(request, 'contact.html')

def checkout(request):
    return render(request, 'checkout.html')

def shop(request):
    return render(request, 'shop.html')

def wishlist(request):
    return render(request, 'wishlist.html')