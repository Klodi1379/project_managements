# Generated by Django 5.0.6 on 2024-07-07 15:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Craft",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("skill_level", models.CharField(max_length=50)),
                ("hourly_rate", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Equipment",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("model_number", models.CharField(max_length=100)),
                ("manufacturer", models.CharField(max_length=100)),
                (
                    "rental_cost_per_day",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Material",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("unit", models.CharField(max_length=50)),
                ("unit_cost", models.DecimalField(decimal_places=2, max_digits=10)),
                ("stock_quantity", models.PositiveIntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="SubContractor",
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
                ("name", models.CharField(max_length=255)),
                ("contact_person", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("email", models.EmailField(max_length=254)),
                ("specialization", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]