from app.payments.models import Payment
from rest_framework import mixins
from rest_framework import viewsets, generics
from .serializers import PaymentSerializer, UserRecognitionSerializer
from app.users.models import User


class PaymentViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    serializer_class = PaymentSerializer

    def get_queryset(self):
        user = self.request.user
        return user.payments.all()



class UserEatInView(generics.CreateAPIView):
    serializer_class = UserRecognitionSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        user = User.objects.get(id=data['user_id'])
        payment = Payment.objects.filter(user=user).order_by('-id')[0]
        if self.request.user.is_staff and not payment.is_completed:
            payment.tax_rate = 10
            payment.save()


user_eat_in_view = UserEatInView.as_view()


class UserStoreExitView(generics.CreateAPIView):
    serializer_class = UserRecognitionSerializer

    def perform_create(self, serializer):
        data = serializer.validated_data
        user = User.objects.get(id=data['user_id'])
        payment = Payment.objects.filter(user=user).order_by('-id')[0]
        if self.request.user.is_staff and not payment.is_completed:
            payment.is_completed = True
            payment.save()


user_store_exit_view = UserStoreExitView.as_view()

