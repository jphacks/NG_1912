from rest_framework import serializers
from app.payments.models import (
    Payment,
    PaymentChoice
)


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'user_id', 'price', 'tax_rate', 'is_completed']
