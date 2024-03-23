import pytest
from django.db import models
from pytest_django import asserts

from django_query_condition_demo.apps.book.models import Book


@pytest.mark.django_db
def test_queryset_statisfy_each_condition_at_least_once_all_conditions_match():
    book = Book.objects.create(name="Book 1", pages=50)
    book2 = Book.objects.create(name="Book 2", pages=100)
    book3 = Book.objects.create(name="Book 3", pages=200)
    Book.objects.create(name="Book 4", pages=300)

    with asserts.assertNumQueries(2):
        # 1. count each condition
        # 2. union query sets matching conditions
        conditions = (
            models.Q(pages=50),
            models.Q(name="Book 2") | models.Q(pages__range=(100, 200)),
        )
        actual = Book.objects.statisfy_each_condition_at_least_once(conditions)

        asserts.assertQuerySetEqual(actual, [book, book2, book3], ordered=False)


@pytest.mark.django_db
def test_queryset_statisfy_each_condition_at_least_once_one_condition_not_match():
    Book.objects.create(name="Book 1", pages=50)
    Book.objects.create(name="Book 2", pages=100)
    Book.objects.create(name="Book 3", pages=200)
    Book.objects.create(name="Book 4", pages=300)

    with asserts.assertNumQueries(1):
        # 1. count each condition
        conditions = (
            models.Q(name="Book 5"),
            models.Q(name="Book 2") | models.Q(pages__range=(100, 200)),
        )
        actual = Book.objects.statisfy_each_condition_at_least_once(conditions)

        asserts.assertQuerySetEqual(actual, [])
