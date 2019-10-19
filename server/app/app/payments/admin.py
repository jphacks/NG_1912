from django.contrib import admin
from .models import (
    Payment,
    PaymentChoice
)

admin.site.register(Payment)
admin.site.register(PaymentChoice)
