from django.contrib.auth import get_user_model
from django.db import models

from competitions.models import Competition
from entries.models import Entry
from sponsors.models import Prize
from teams.models import Team


User = get_user_model()


class Judge(models.Model):
    user = models.ForeignKey(
        User,
        related_name="judging",
        on_delete=models.CASCADE,
    )
    competition = models.ForeignKey(
        Competition,
        related_name="judges",
        on_delete=models.CASCADE,
    )
    bio = models.TextField(blank=True, default="")
    created = models.DateTimeField(blank=True, auto_now_add=True, db_index=True)
    updated = models.DateTimeField(blank=True, auto_now=True, db_index=True)

    def __str__(self):
        return f"{self.user.get_full_name()} for {self.competition.name}"


class Score(models.Model):
    CATEGORY_CODE = "code_quality"
    CATEGORY_DESIGN = "design"
    CATEGORY_IDEA = "idea"
    CATEGORY_EXECUTION = "execution"
    CATEGORY_CHOICES = [
        [CATEGORY_CODE, "Code Quality"],
        [CATEGORY_DESIGN, "Design"],
        [CATEGORY_IDEA, "Idea"],
        [CATEGORY_EXECUTION, "Execution"],
    ]

    competition = models.ForeignKey(
        Competition,
        related_name="scores",
        on_delete=models.CASCADE,
    )
    judge = models.ForeignKey(
        Judge,
        related_name="scores",
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name="scores",
        on_delete=models.CASCADE,
    )
    category = models.CharField(
        max_length=32,
        choices=CATEGORY_CHOICES,
        default=CATEGORY_CODE,
    )
    score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        default="0.0",
        help_text=(
            "Values 1-5. Decimals allowed, up to two decimal places (e.g. `2.25`).",
        ),
    )
    created = models.DateTimeField(blank=True, auto_now_add=True, db_index=True)
    updated = models.DateTimeField(blank=True, auto_now=True, db_index=True)

    class Meta:
        unique_together = [
            "competition",
            "judge",
            "entry",
            "category",
        ]

    def __str__(self):
        return (
            f"{self.entry} scored "
            f"{self.get_category_display()}: {self.score} "
            f"by {self.judge.username}"
        )


class Result(models.Model):
    competition = models.ForeignKey(
        Competition,
        related_name="results",
        on_delete=models.CASCADE,
    )
    team = models.ForeignKey(
        Team,
        related_name="results",
        on_delete=models.CASCADE,
    )
    entry = models.ForeignKey(
        Entry,
        related_name="results",
        on_delete=models.CASCADE,
    )
    prizes = models.ManyToManyField(
        Prize,
        related_name="results",
        on_delete=models.CASCADE,
    )
    # Denorm the score totals to save on queries for scoreboards.
    code_quality_score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        default="0.0",
        help_text=(
            "Values 1-5. Decimals allowed, up to two decimal places (e.g. `2.25`).",
        ),
    )
    design_score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        default="0.0",
        help_text=(
            "Values 1-5. Decimals allowed, up to two decimal places (e.g. `2.25`).",
        ),
    )
    idea_score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        default="0.0",
        help_text=(
            "Values 1-5. Decimals allowed, up to two decimal places (e.g. `2.25`).",
        ),
    )
    execution_score = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        default="0.0",
        help_text=(
            "Values 1-5. Decimals allowed, up to two decimal places (e.g. `2.25`).",
        ),
    )
    created = models.DateTimeField(blank=True, auto_now_add=True, db_index=True)
    updated = models.DateTimeField(blank=True, auto_now=True, db_index=True)

    class Meta:
        unique_together = [
            "competition",
            "team",
            "entry",
        ]

    def __str__(self):
        return f"{self.team.name}: {self.entry.name} in {self.competition.name}"
