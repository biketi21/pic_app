from django.db import models
from accounts.models import Account



# Create your models here.

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class ImageUpload(models.Model):
    images = models.ImageField(upload_to=user_directory_path)
    event_name = models.CharField(max_length=50)
    event_id = models.CharField(max_length=10)
    user = models.ForeignKey(Account, on_delete=models.PROTECT)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    Likes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.event_name
