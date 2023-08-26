from filmRating.models import *
from django.db.models import Sum, Count


class Film(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="films_created"
    )
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    img = models.ImageField(null=True, blank=True)
    category = models.ManyToManyField(Category, related_name="films_categories")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    @property
    def stars(self):
        data = self.ratings.aggregate(Sum("value"), Count("id"))
        if data["id__count"] < 1:
            return "Sem Avaliações"

        stars = data["value__sum"] / data["id__count"]
        stars = round(stars, 2)
        return stars
