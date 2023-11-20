from django.contrib.auth import get_user_model
from django.db import models

from competitions.models import Competition
from teams.models import (
    Team,
    TeamMember,
)
from utils.gravatars import gravatar_url
from utils.querysets import ActiveQuerySet


User = get_user_model()


class ActiveEntryQuerySet(ActiveQuerySet):
    pass


class Entry(models.Model):
    competition = models.ForeignKey(
        Competition,
        related_name="entries",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Team,
        related_name="entries",
        on_delete=models.CASCADE,
    )
    team_members = models.ManyToManyField(
        TeamMember,
        related_name="entries",
    )
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, default="")
    repository_url = models.URLField(blank=True, null=True, db_index=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = ActiveEntryQuerySet.as_manager()

    def __str__(self):
        return (
            f"{self.name} ({self.team.name}): {self.url} "
            f"for '{self.competition.name}'"
        )

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()


class Commit(models.Model):
    entry = models.ForeignKey(
        Entry,
        related_name="commits",
        on_delete=models.CASCADE,
    )
    committer = models.ForeignKey(
        TeamMember,
        related_name="commits",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    commit_id = models.CharField(
        max_length=64,
        db_index=True,
        help_text="Just the SHA or equivalent, please",
    )
    email = models.EmailField(db_index=True)
    message = models.TextField(blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.email} committed {self.commit_id}: {self.short_message()}"

    def short_message(self, max_length=32):
        if len(self.message) <= max_length:
            return self.message

        return self.message[:max_length] + "..."

    def gravatar(self):
        return gravatar_url(self.email, size=60)
