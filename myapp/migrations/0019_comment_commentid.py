# Generated by Django 5.0.3 on 2024-04-30 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0018_alter_commentchild_tag"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="Commentid",
            field=models.IntegerField(default=1),
        ),
    ]