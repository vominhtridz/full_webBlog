# Generated by Django 5.0.3 on 2024-05-06 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0032_alter_userprofile_phone_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="gender",
            field=models.CharField(
                choices=[("Nam", "Nam"), ("Nữ", "Nữ"), ("Khác", "Khác")],
                default="Nam",
                max_length=20,
            ),
        ),
    ]