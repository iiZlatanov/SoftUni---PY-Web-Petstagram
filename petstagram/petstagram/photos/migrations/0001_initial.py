# Generated by Django 4.2.20 on 2025-04-03 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("pets", "0002_pet_delete_pets"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("photo", models.ImageField(upload_to="pet_photos/")),
                (
                    "description",
                    models.TextField(
                        blank=True,
                        max_length=300,
                        null=True,
                        validators=[django.core.validators.MinLengthValidator(10)],
                    ),
                ),
                ("location", models.CharField(blank=True, max_length=30, null=True)),
                ("pets", models.ManyToManyField(to="pets.pet")),
            ],
        ),
    ]
