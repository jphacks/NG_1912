from django.db.models import (
    PositiveIntegerField,
    CharField,
    Model
)


class Food(Model):
    name = CharField(max_length=100, unique=True)
    price = PositiveIntegerField(blank=True, default=0)
