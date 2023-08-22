from django.contrib import admin
from .models import *


class FilmAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "owner",
        "list_display_category",
        "created_at",
    ]
    # readonly_fields = [
    #     "owner",
    # ]

    search_fields = [
        "name",
    ]

    list_filter = [
        "category",
    ]

    def list_display_category(self, obj):
        return [i.name for i in obj.category.all()]


class RatingAdmin(admin.ModelAdmin):
    list_display = [
        "film_rated",
        "user",
    ]

    # readonly_fields = [
    #     "user",
    # ]

    search_fields = [
        "user__username",
        "film_rated__name",
    ]


class ProfileAdmin(admin.ModelAdmin):
    search_fields = [
        "user__username",
    ]

    readonly_fields = [
        "favorites",
    ]


class CategoryAdmin(admin.ModelAdmin):
    search_fields = [
        "name",
    ]


# Register your models here.

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Rating, RatingAdmin)
admin.site.register(Film, FilmAdmin)
admin.site.register(Category, CategoryAdmin)
