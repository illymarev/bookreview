from django.contrib import admin
from .models import BookModel, Comment, Quote


# Register your models here.
@admin.register(BookModel)
class BookModelAdmin(admin.ModelAdmin):
    search_fields = ['title']

    list_filter = ['release_year', 'length']

    list_display = ['title', 'release_year', 'length']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['name', 'text', 'book', 'created_on']
    list_filter = ['created_on']
    search_fields = ['name', 'text']

@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    search_fields = ['text']


