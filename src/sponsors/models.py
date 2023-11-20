from django.db import models

from competitions.models import Competition


class Sponsor(models.Model):
    name = models.CharField(max_length=64)
    url = models.URLField(blank=True, null=True)
    # FIXME: I don't feel like dealing with uploads/media yet.
    # logo = models.ImageField(
    #
    # )
    description = models.TextField(blank=True, default="")
    competitions = models.ManyToManyField(
        Competition,
        related_name="sponsors",
    )
    created = models.DateTimeField(blank=True, auto_now_add=True, db_index=True)
    updated = models.DateTimeField(blank=True, auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.name}"


class Prize(models.Model):
    PLACE_FIRST = "first"
    PLACE_SECOND = "second"
    PLACE_THIRD = "third"
    PLACE_PARTICIPATION = "participation"
    PLACE_CHOICES = [
        [PLACE_FIRST, "First"],
        [PLACE_SECOND, "Second"],
        [PLACE_THIRD, "Third"],
        [PLACE_PARTICIPATION, "Participation"],
    ]

    competition = models.ForeignKey(
        Competition,
        related_name="prizes",
        on_delete=models.CASCADE,
    )
    sponsor = models.ForeignKey(
        Sponsor,
        related_name="prizes",
    )
    name = models.CharField(max_length=128)
    place = models.CharField(
        max_length=16, choices=PLACE_CHOICES, default=PLACE_FIRST, db_index=True
    )
    estimated_value = models.PositiveIntegerField(
        blank=True,
        default=0,
        help_text="This is an internal-only field, to help with prize allocations.",
    )
    created = models.DateTimeField(blank=True, auto_now_add=True, db_index=True)
    updated = models.DateTimeField(blank=True, auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.name}"
