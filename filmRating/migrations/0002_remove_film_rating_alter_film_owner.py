# Generated by Django 4.2.1 on 2023-08-02 22:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("filmRating", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="film",
            name="rating",
        ),
        migrations.AlterField(
            model_name="film",
            name="owner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="films_created",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]