from django.db.models import ManyToManyField
from filmRating.models import *


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = ManyToManyField(Film, related_name="favorites")
    img = models.ImageField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}"

    @receiver(sender=User, signal=post_save)
    def create_post_save(sender, instance, created, **kwargs):
        try:
            if created:
                Profile.objects.create(user=instance)
        except:
            pass

    @receiver(sender=User, signal=post_save)
    def update_post_save(sender, instance, **kwars):
        try:
            instance.profile.save()
        except:
            pass
