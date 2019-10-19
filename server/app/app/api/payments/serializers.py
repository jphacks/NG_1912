from rest_framework import serializers
from app.payments.models import (
    Payment,
    PaymentChoice
)
from app.api.foods.serializers import FoodSerializer


class PaymentChoiceSerializer(serializers.HyperlinkedModelSerializer):
    food = serializers.SerializerMethodField()

    class Meta:
        model = PaymentChoice
        fields = ['id', 'food', 'food_count', 'price']

    def get_food(self, obj):
        return FoodSerializer(obj.food).data


class PaymentSerializer(serializers.HyperlinkedModelSerializer):
    choices = serializers.SerializerMethodField()

    class Meta:
        model = Payment
        fields = ['id', 'user_id', 'price', 'tax_rate', 'is_completed', 'choices']

    def get_choices(self, obj):
        return PaymentChoiceSerializer(obj.choices.all(), many=True).data


class UserRecognitionSerializer(serializers.Serializer):
    user_id = serializers.IntegerField(write_only=True)
