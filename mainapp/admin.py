from django.contrib import admin
from mainapp.models import ImageUpload
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class ImageUploadAdmin(UserAdmin):
    list_display = (
        "event_name",
        "event_id",
        "Likes",
       )
    search_fields = ("event_name", "event_id")
    readonly_fields = ()

    ordering = ('event_name',)

    filter_horizontal = ()
    list_filter = ("user",)
    fieldsets = ()

admin.site.register(ImageUpload, ImageUploadAdmin)