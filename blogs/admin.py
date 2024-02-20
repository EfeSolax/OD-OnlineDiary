from django.contrib import admin
from .models import BlogModel, CommentModel

# Register your models here.

admin.site.register(CommentModel)

@admin.register(BlogModel)
class BlogModels(admin.ModelAdmin):
    class Meta:
        model = BlogModel

    list_display_links = ["title", "created_at"]
    list_display = ["title", "author", "created_at"]
    list_filter = ["created_at"]
    search_fields = ["title", "author"]