from django.db.models import (
    BooleanField,
    PositiveIntegerField,
    PositiveSmallIntegerField,
    SET_NULL,
    CASCADE,
    ForeignKey,
    Model
)
from app.users.models import User
from app.foods.models import Food


class Payment(Model):
    user = ForeignKey(User, on_delete=SET_NULL, null=True, related_name="payments")
    price = PositiveIntegerField(blank=True, default=0)
    tax_rate = PositiveSmallIntegerField(blank=True, default=0)
    is_completed = BooleanField(default=False)


class PaymentChoice(Model):
    payment = ForeignKey(Payment, on_delete=CASCADE, null=True, related_name="choices")
    food = ForeignKey(Food, on_delete=SET_NULL, null=True, related_name="byPaymentChoices")
    food_count = PositiveSmallIntegerField(blank=True, default=1)
    price = PositiveIntegerField(blank=True, default=0)
