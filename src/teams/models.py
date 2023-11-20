from django.contrib.auth import get_user_model
from django.db import models
from django.utils.text import slugify

from competitions.models import Competition
from utils.querysets import ActiveQuerySet


User = get_user_model()


class ActiveTeamQuerySet(ActiveQuerySet):
    pass


class ActiveTeamMemberQuerySet(ActiveQuerySet):
    pass


class Team(models.Model):
    name = models.CharField(max_length=128)
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    owner = models.ForeignKey(
        User,
        related_name="owned_teams",
        on_delete=models.CASCADE,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = ActiveTeamQuerySet.as_manager()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()

    def members_for_competition(self, competition):
        return self.team_members.filter(competitions=competition).order_by(
            "user__username"
        )


class TeamMember(models.Model):
    team = models.ForeignKey(
        Team,
        related_name="members",
        on_delete=models.CASCADE,
    )
    user = models.ForeignKey(
        User,
        related_name="teams",
        on_delete=models.CASCADE,
    )
    competitions = models.ManyToManyField(
        Competition,
        related_name="team_members",
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = ActiveTeamMemberQuerySet.as_manager()

    class Meta:
        unique_together = [
            "team",
            "user",
        ]

    def __str__(self):
        return f"{self.user.username} on {self.team.name}"

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
