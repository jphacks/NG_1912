from app.foods.models import Food
from rest_framework import viewsets
from .serializers import FoodSerializer


class FoodViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
