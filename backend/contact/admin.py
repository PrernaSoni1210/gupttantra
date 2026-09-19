from django.contrib import admin
from .models import ContactMessage


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):

    list_display = (
        'name',
        'email',
        'phone',
        'consultation_type',
        'created_at',
    )

    search_fields = (
        'name',
        'email',
        'phone',
        'consultation_type',
    )

    list_filter = (
        'consultation_type',
        'created_at',
    )

    ordering = ('-created_at',)