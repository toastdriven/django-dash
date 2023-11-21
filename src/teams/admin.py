from django.contrib import admin

from .models import (
    Team,
    TeamMember,
)


class TeamAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "name",
        "slug",
        "owner",
        "is_deleted",
        "created",
    ]
    list_filter = [
        "is_deleted",
    ]
    raw_id_fields = ["owner"]
    search_fields = [
        "name",
        "slug",
        "owner__username",
        "owner__email",
    ]


class TeamMemberAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "user",
        "team",
        "is_deleted",
        "created",
    ]
    list_filter = [
        "competitions",
        "is_deleted",
    ]
    raw_id_fields = [
        "competitions",
        "team",
        "user",
    ]
    search_fields = [
        "user__username",
        "user__email",
        "team__name",
        "competitions__name",
    ]


admin.site.register(Team, TeamAdmin)
admin.site.register(TeamMember, TeamMemberAdmin)
