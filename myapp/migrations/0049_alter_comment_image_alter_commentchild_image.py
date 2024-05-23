# Generated by Django 5.0.3 on 2024-05-10 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0048_remove_comment_author_remove_commentchild_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="image",
            field=models.ImageField(
                default="/static/images/user-icon.png", upload_to="comment/images"
            ),
        ),
        migrations.AlterField(
            model_name="commentchild",
            name="image",
            field=models.ImageField(
                default="/static/images/user-icon.png", upload_to="comment/images"
            ),
        ),
    ]
