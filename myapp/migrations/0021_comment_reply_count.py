# Generated by Django 5.0.3 on 2024-04-30 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0020_comment_like_commentchild_like"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="reply_count",
            field=models.IntegerField(default=0),
        ),
    ]
