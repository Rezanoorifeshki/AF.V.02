from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'coreapp/index.html')

def about(request):
    return render(request, 'coreapp/aboutus.html')

def contact(request):
    return render(request, 'coreapp/contactus.html')