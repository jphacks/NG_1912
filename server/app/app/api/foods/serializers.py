from rest_framework import serializers
from app.foods.models import Food


class FoodSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'name', 'price']
