# Generated by Django 4.2.20 on 2025-04-03 16:30

from django.db import migrations, models
import petstagram.photos.models


class Migration(migrations.Migration):

    dependencies = [
        ("photos", "0002_petphoto_delete_photo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="petphoto",
            name="photo",
            field=models.ImageField(
                upload_to="pet_photos/",
                validators=[
                    petstagram.photos.models.MaxFileSizeValidator(limit_value=5242880)
                ],
            ),
        ),
    ]
