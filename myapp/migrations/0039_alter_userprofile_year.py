# Generated by Django 5.0.3 on 2024-05-06 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0038_alter_userprofile_day_alter_userprofile_month_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="year",
            field=models.IntegerField(default=2024),
        ),
    ]
