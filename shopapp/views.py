from django.shortcuts import render

# Create your views here.
def shop (request):
    return render(request, 'shopapp/shop.html')

def shopproduct (request):
    return render(request, 'shopapp/shopproduct.html')

def wishlist (request):
    return render(request, 'shopapp/wishlist.html')