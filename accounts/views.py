from django.shortcuts import render
from django.contrib.auth import logout

# Create your views here.


def logout(request):
    logout(request)
    return print("logged out")
