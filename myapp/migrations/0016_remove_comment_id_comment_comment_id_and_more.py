# Generated by Django 5.0.3 on 2024-04-29 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0015_commentchild"),
    ]

    operations = [

        migrations.AddField(
            model_name="commentchild",
            name="commentChild_id",
            field=models.IntegerField(default=1),
        ),
    ]
