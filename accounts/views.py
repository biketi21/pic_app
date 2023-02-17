from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import logout
from django.conf import settings
from accounts.models import BrandInfo

# Create your views here.


def complete_profile(request):

    if request.method == "POST":
        brand_info = BrandInfo.objects.create(
            user=request.user,
            brand_name=request.POST["brand_name"],
            brand_tagline=request.POST["tagline"],
            brand_logo=request.FILES["brand_logo"],
            brand_address=request.POST["address"],
            brand_phone=request.POST["phone_no"],
            brand_email=request.POST["brand_email"],
            instagram_profile=request.POST["brand_instagram"],
        )
        return redirect(settings.LOGIN_REDIRECT_URL)

    return render(request, "complete-profile.html")


def logout(request):
    logout(request)
    return print("logged out")
