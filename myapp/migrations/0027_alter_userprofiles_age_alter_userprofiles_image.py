# Generated by Django 5.0.3 on 2024-05-05 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0026_userprofiles_delete_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofiles",
            name="age",
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name="userprofiles",
            name="image",
            field=models.ImageField(upload_to="profiles/images"),
        ),
    ]