from django.contrib import admin

from .models import (
    Sponsor,
    Prize,
)


class SponsorAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "name",
        "url",
        "description",
        "created",
    ]
    list_filter = []
    raw_id_fields = [
        "competitions",
    ]
    search_fields = [
        "name",
        "description",
    ]


class PrizeAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "name",
        "sponsor",
        "place",
        "competition",
        "bio",
        "created",
    ]
    list_filter = [
        "place",
        "competition",
    ]
    raw_id_fields = [
        "competition",
        "sponsor",
    ]
    search_fields = [
        "name",
        "sponsor__name",
        "competition__name",
    ]


admin.site.register(Sponsor, SponsorAdmin)
admin.site.register(Prize, PrizeAdmin)
