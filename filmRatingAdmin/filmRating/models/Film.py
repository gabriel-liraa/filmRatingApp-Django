from filmRating.models import *


class Film(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="films_created"
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    category = models.ManyToManyField(Category, related_name="films_categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"
