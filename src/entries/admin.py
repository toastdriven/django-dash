from django.contrib import admin

from .models import (
    Entry,
    Commit,
)


class EntryAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "name",
        "team",
        "url",
        "competition",
        "is_deleted",
        "created",
    ]
    list_filter = [
        "is_deleted",
    ]
    raw_id_fields = [
        "competition",
        "team",
        "team_members",
    ]
    search_fields = [
        "name",
        "team__name",
        "competition__name",
    ]


class CommitAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "commit_id",
        "email",
        "message",
        "entry",
        "created",
    ]
    list_filter = []
    raw_id_fields = [
        "entry",
        "committer",
    ]
    search_fields = [
        "entry__name",
        "email",
        "message",
    ]


admin.site.register(Entry, EntryAdmin)
admin.site.register(Commit, CommitAdmin)
