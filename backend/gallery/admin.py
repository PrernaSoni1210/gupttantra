from django.contrib import admin
from django.utils.html import format_html
from .models import GalleryImage


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'image_preview',
        'created_at',
    )

    search_fields = (
        'title',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'image_preview',
    )

    def image_preview(self, obj):

        if obj.image:
            return format_html(
                '<img src="{}" width="100" height="70" '
                'style="object-fit: cover; border-radius: 5px;" />',
                obj.image.url
            )

        return "No image"

    image_preview.short_description = "Image Preview"