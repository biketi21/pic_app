from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path('display-images', views.display_upload, name='display-images')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
