# Generated by Django 4.1.4 on 2023-02-05 22:31

from django.db import migrations, models
import mainapp.models


class Migration(migrations.Migration):

    dependencies = [
        ("mainapp", "0002_imageupload_event_name_alter_imageupload_images"),
    ]

    operations = [
        migrations.AlterField(
            model_name="imageupload",
            name="images",
            field=models.ImageField(upload_to=mainapp.models.user_directory_path),
        ),
    ]