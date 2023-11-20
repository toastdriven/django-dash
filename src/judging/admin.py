from django.contrib import admin

from .models import (
    Judge,
    Score,
    Result,
)


class JudgeAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "user",
        "competition",
        "bio",
        "created",
    ]
    list_filter = [
        "competition",
    ]
    raw_id_fields = [
        "competition",
        "user",
    ]
    search_fields = [
        "user__username",
        "competition__name",
    ]


class ScoreAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "entry",
        "judge",
        "competition",
        "category",
        "score",
        "created",
    ]
    list_filter = [
        "category",
        "competition",
    ]
    raw_id_fields = [
        "competition",
        "judge",
        "entry",
    ]
    search_fields = [
        "entry__name",
        "judge__user__username",
        "competition__name",
    ]


class ResultAdmin(admin.ModelAdmin):
    date_hierarchy = "created"
    list_display = [
        "entry",
        "team",
        "competition",
        "code_quality_score",
        "design_score",
        "idea_score",
        "execution_score",
        "created",
    ]
    list_filter = [
        "competition",
    ]
    raw_id_fields = [
        "competition",
        "team",
        "entry",
    ]
    search_fields = [
        "entry__name",
        "team__name",
        "competition__name",
    ]


admin.site.register(Judge, JudgeAdmin)
admin.site.register(Score, ScoreAdmin)
admin.site.register(Result, ResultAdmin)
