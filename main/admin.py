from django.contrib import admin

from .models import Post
from .models import Category
from django.utils.html import format_html

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'image_tag', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('created_at', 'updated_at')
    search_fields = ('title', 'content')
    list_editable = ('author', )
    def image_tag(self, obj):
            if obj.image:
                return format_html(
                    '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 4px" />',
                    obj.image.url,
                )
            return format_html('<span>не має зображення</span>')
        
    image_tag.short_description = "Image"
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}