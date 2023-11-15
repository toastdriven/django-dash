from django.contrib import admin

from .models import Competition


class CompetitionAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "name",
        "slug",
        "signup_start_date",
        "contest_start_date",
        "judging_start_date",
        "is_deleted",
        "created",
    ]
    list_filter = [
        "is_deleted",
    ]
    search_fields = [
        "name",
    ]


admin.site.register(Competition, CompetitionAdmin)
