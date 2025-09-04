from django.contrib import admin
from .models import ContactSubmission

@admin.register(ContactSubmission)
class ContactSubmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'submitted_at', 'is_read']
    list_filter = ['is_read', 'submitted_at']
    readonly_fields = ['submitted_at']
    list_editable = ['is_read']