# Generated by Django 5.0.3 on 2024-05-01 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0021_comment_reply_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="father",
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name="comment",
            name="reply_count",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
