from django.db import models
from accounts.models import Account

# Create your models here.
class ImageUpload(models.Model):
    images = models.ImageField()
    event_name = models.CharField(max_length=50)
    event_id = models.CharField(max_length=10)
    user = models.ForeignKey(Account, on_delete=models.PROTECT)
    date_uploaded = models.DateTimeField(auto_now_add=True)
    Likes = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.event_name
