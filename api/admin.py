from django.contrib import admin

from .models import (
    Category, Recipe, Review, Upvote
)

admin.site.register(Category)
admin.site.register(Recipe)
admin.site.register(Review)
admin.site.register(Upvote)
