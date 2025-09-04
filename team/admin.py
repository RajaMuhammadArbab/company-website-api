from django.contrib import admin
from .models import TeamMember

@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'role', 'email', 'order', 'is_active']
    list_editable = ['order', 'is_active']
    list_filter = ['is_active']