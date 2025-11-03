from django.shortcuts import render

# Create your views here.
def account(request):
    return render(request, 'usersapp/account.html')

def login(request):
    return render(request, 'usersapp/login.html')