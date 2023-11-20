from django.contrib import admin

from .models import Invite


class InviteAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "to_email",
        "sent_by",
        "team",
        "accepted",
        "created",
    ]
    list_filter = [
        "accepted",
    ]
    raw_id_fields = [
        "team",
        "sent_by",
    ]
    search_fields = [
        "team__name",
        "sent_by__username",
        "sent_by__email",
        "to_email",
    ]


admin.site.register(Invite, InviteAdmin)
