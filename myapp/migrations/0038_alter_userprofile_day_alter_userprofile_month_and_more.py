# Generated by Django 5.0.3 on 2024-05-06 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0037_alter_userprofile_email"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="day",
            field=models.IntegerField(
                choices=[
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                    (12, 12),
                    (13, 13),
                    (14, 14),
                    (15, 15),
                    (16, 16),
                    (17, 17),
                    (18, 18),
                    (19, 19),
                    (20, 20),
                    (21, 21),
                    (22, 22),
                    (23, 23),
                    (24, 24),
                    (25, 25),
                    (26, 26),
                    (27, 27),
                    (28, 28),
                    (29, 29),
                    (30, 30),
                    (31, 31),
                ],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="month",
            field=models.IntegerField(
                choices=[
                    (1, 1),
                    (2, 2),
                    (3, 3),
                    (4, 4),
                    (5, 5),
                    (6, 6),
                    (7, 7),
                    (8, 8),
                    (9, 9),
                    (10, 10),
                    (11, 11),
                    (12, 12),
                ],
                default=1,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="year",
            field=models.IntegerField(choices=[], default=2024),
        ),
    ]
