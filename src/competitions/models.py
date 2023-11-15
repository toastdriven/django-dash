from django.db import models
from django.utils.text import slugify

from utils.querysets import ActiveQuerySet


class ActiveCompetitionQuerySet(ActiveQuerySet):
    pass


class Competition(models.Model):
    name = models.CharField(max_length=64)
    slug = models.SlugField(blank=True, unique=True, db_index=True)
    signup_start_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    signup_end_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    contest_start_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    contest_end_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    judging_start_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    judging_end_date = models.DateTimeField(
        blank=True,
        null=True,
        db_index=True,
    )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_deleted = models.BooleanField(default=False)

    objects = ActiveCompetitionQuerySet.as_manager()

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.is_deleted = True
        self.save()
