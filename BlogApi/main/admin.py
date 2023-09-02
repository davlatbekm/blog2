from django.contrib import admin
from django.utils.safestring import mark_safe

# Register your models here.
from .models import Post, Comments


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["user", 'get_image', "description"]
    list_filter = ('user',  'description')
    search_fields = ('user', 'description')
    ordering = ("user",)

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="75">')
        else:
            return "Фото пока нет"

    get_image.short_description = "Миниатюра"


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', "post_id", "text"]
    list_filter = ('user', 'post_id', 'text')
    search_fields = ('post_id', 'text')
    ordering = ("post_id",)
