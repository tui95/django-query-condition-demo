from __future__ import annotations

from typing import Sequence

from django.db import models


class BookQuerySet(models.QuerySet):
    def statisfy_each_condition_at_least_once(
        self,
        conditions: Sequence[models.Q],
    ) -> models.QuerySet:
        each_condition_matched_count = self.aggregate(
            **{
                f"condition{index}_count": models.Count("id", filter=condition)
                for index, condition in enumerate(conditions)
            }
        )
        if not all(count >= 1 for count in each_condition_matched_count.values()):
            return self.none()
        return self.none().union(*(self.filter(condition) for condition in conditions))


class Book(models.Model):
    name = models.CharField(max_length=50, unique=True)
    pages = models.PositiveIntegerField()

    objects = BookQuerySet.as_manager()

    def __str__(self) -> str:
        return self.name
