from django.shortcuts import render

# Create your views here.
def cart(request):
    return render(request, 'orderapp/cart.html')

def checkout(request):
    return render(request, 'orderapp/checkout.html')

def order(request):
    return render(request, 'orderapp/order.html')