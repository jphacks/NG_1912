from app.payments.models import Payment
from rest_framework import viewsets
from .serializers import PaymentSerializer
from rest_framework import mixins


class PaymentViewSet(mixins.ListModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

