# Generated by Django 4.1.1 on 2023-04-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("Stores", "0002_delete_sliderimage"),
    ]

    operations = [
        migrations.CreateModel(
            name="Items",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("item_name", models.CharField(max_length=255)),
                ("item_rate", models.CharField(max_length=255)),
                ("item_image", models.ImageField(upload_to="items")),
            ],
        ),
    ]
