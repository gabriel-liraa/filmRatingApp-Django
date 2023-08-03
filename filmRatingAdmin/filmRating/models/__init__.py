from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from filmRating.models.Category import Category
from filmRating.models.Film import Film
from filmRating.models.Rating import Rating
from filmRating.models.Profile import Profile
