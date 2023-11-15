from django.contrib import admin

from .models import (
    Repository,
    Commit,
)


class RepositoryAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "team",
        "name",
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
        "repository",
        "created",
    ]
    list_filter = []
    raw_id_fields = [
        "repository",
        "committer",
    ]
    search_fields = [
        "repository__name",
        "email",
        "message",
    ]


admin.site.register(Repository, RepositoryAdmin)
admin.site.register(Commit, CommitAdmin)
