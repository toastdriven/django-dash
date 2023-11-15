from django.db import models


class ActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_deleted=False)
