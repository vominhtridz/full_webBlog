# Generated by Django 5.0.3 on 2024-05-19 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0060_remove_userprofile_user_alter_post_author"),
    ]

    operations = [
        migrations.CreateModel(
            name="Notification",
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
                ("user_id", models.IntegerField(default=1)),
                ("message", models.CharField(default="", max_length=100)),
            ],
        ),
    ]
