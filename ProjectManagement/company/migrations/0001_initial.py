# Generated by Django 5.0.6 on 2024-07-07 15:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=17,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.",
                                regex="^\\+?1?\\d{9,15}$",
                            )
                        ],
                    ),
                ),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("name", models.CharField(max_length=255)),
                ("slug", models.SlugField(blank=True, unique=True)),
                ("register_name", models.CharField(max_length=255)),
                ("address", models.TextField()),
                ("post_code", models.CharField(max_length=10)),
                ("fax_number", models.CharField(blank=True, max_length=20)),
                ("website", models.URLField(blank=True)),
            ],
            options={
                "verbose_name_plural": "Companies",
                "ordering": ["name"],
            },
        ),
    ]