from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import logout

# Create your views here.

def complete_profile(request):
    return render(request, 'complete-profile.html')
def logout(request):
    logout(request)
    return print("logged out")
