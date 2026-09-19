from django.contrib import admin
from django.utils.html import format_html
from .models import Video


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'video_type',
        'thumbnail_preview',
        'created_at',
    )

    search_fields = (
        'title',
        'video_url',
    )

    list_filter = (
        'created_at',
    )

    ordering = (
        '-created_at',
    )

    readonly_fields = (
        'thumbnail_preview',
    )

    def video_type(self, obj):

        if obj.video_file:
            return "Desktop / Local Video"

        elif obj.video_url:
            return "YouTube Video"

        return "No Video"

    video_type.short_description = "Video Type"

    def thumbnail_preview(self, obj):

        # YouTube thumbnail
        if obj.video_url:

            thumbnail_url = obj.youtube_thumbnail_url

            if thumbnail_url:

                return format_html(
                    '<img src="{}" width="160" height="90" '
                    'style="object-fit: cover; border-radius: 6px;" />',
                    thumbnail_url
                )

        # Local video thumbnail
        if obj.thumbnail:

            return format_html(
                '<img src="{}" width="160" height="90" '
                'style="object-fit: cover; border-radius: 6px;" />',
                obj.thumbnail.url
            )

        # Local video without thumbnail
        if obj.video_file:

            return format_html(
                '<video width="160" height="90" controls '
                'style="object-fit: cover; border-radius: 6px;">'
                '<source src="{}">'
                '</video>',
                obj.video_file.url
            )

        return "No preview"

    thumbnail_preview.short_description = "Thumbnail / Preview"