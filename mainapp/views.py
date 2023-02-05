from django.shortcuts import render
from django.http import HttpResponse
from .models import ImageUpload
from accounts.models import Account
import shortuuid

# Create your views here.

def home(request):

    if request.method == "POST":
        images = request.FILES.getlist("images")
        event_id = shortuuid.ShortUUID().random(length=6)
        event_name = request.POST['event_name']

        for image in images:
            new_image = ImageUpload.objects.create(
                images=image,
                event_id=event_id,
                user_id=request.user.id,
                event_name = event_name,
            )
            new_image.save()

    return render(request, "index.html")

def display_upload(request):
    context = {}
    if request.method == 'POST':
        event_id = request.POST['event_id']
        photo = ImageUpload.objects.filter(event_id=event_id)

        return render(request, 'display-upload.html', {'photos': photo} )

    return render(request, 'display-upload.html')

