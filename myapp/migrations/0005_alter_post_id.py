# Generated by Django 5.0.3 on 2024-04-24 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0004_post_topic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
