# Generated by Django 4.2.3 on 2023-08-22 13:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("filmRating", "0003_film_img"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="img",
            field=models.ImageField(blank=True, null=True, upload_to=""),
        ),
    ]
