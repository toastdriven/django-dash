from django.contrib.auth import get_user_model
from django.db import models

from teams.models import Team

from utils import codes


User = get_user_model()


class Invite(models.Model):
    team = models.ForeignKey(
        Team,
        related_name="invites",
        on_delete=models.CASCADE,
    )
    sent_by = models.ForeignKey(
        User,
        related_name="sent_invites",
        on_delete=models.CASCADE,
    )
    to_email = models.EmailField(db_index=True)
    accepted = models.BooleanField(
        default=None,
        blank=True,
        null=True,
        db_index=True,
        help_text="Null means unopened. True is accepted, False is rejected.",
    )
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team.name} invited {self.email}: {self.accepted}"

    def save(self, *args, **kwargs):
        if not self.accept_code:
            self.accept_code = codes.generate_code()

        return super().save(*args, **kwargs)
