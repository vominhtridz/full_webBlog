# Generated by Django 5.0.3 on 2024-05-05 02:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0025_rename_userprofiles_userprofile"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserProfiles",
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
                ("age", models.CharField(blank=True, max_length=30)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=11, null=True),
                ),
                ("defaultName", models.CharField(blank=True, max_length=30)),
                ("image", models.ImageField(upload_to="images")),
                ("email", models.EmailField(blank=True, max_length=254)),
                ("gender", models.CharField(default="Nam", max_length=20)),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
