# Generated by Django 4.1.4 on 2023-02-17 12:48

import accounts.models
from django.db import migrations, models
import shortuuid.django_fields


class Migration(migrations.Migration):

    dependencies = [
        ("accounts", "0002_brandinfo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="id",
            field=shortuuid.django_fields.ShortUUIDField(
                alphabet="abcDEfG7890",
                length=6,
                max_length=7,
                prefix="id_",
                primary_key=True,
                serialize=False,
            ),
        ),
        migrations.AlterField(
            model_name="brandinfo",
            name="brand_logo",
            field=models.ImageField(upload_to=accounts.models.user_directory_path),
        ),
    ]
