# Generated by Django 5.0.3 on 2024-05-05 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0030_rename_userprofiles_userprofile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="day",
            field=models.CharField(
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
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="month",
            field=models.CharField(
                choices=[
                    (1, "Tháng 1"),
                    (2, "Tháng 2"),
                    (3, "Tháng 3"),
                    (4, "Tháng 4"),
                    (5, "Tháng 5"),
                    (6, "Tháng 6"),
                    (7, "Tháng 7"),
                    (8, "Tháng 8"),
                    (9, "Tháng 9"),
                    (10, "Tháng 10"),
                    (11, "Tháng 11"),
                    (12, "Tháng 12"),
                ],
                default="Tháng 1",
                max_length=30,
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="year",
            field=models.CharField(choices=[], default=2024, max_length=30),
        ),
    ]