from django.urls import path, include
from rest_framework import routers
from app.api.users.views import UserViewSet
from app.api.payments.views import (
    PaymentViewSet,
    user_eat_in_view,
    user_store_exit_view
)

app_name = "api"

router = routers.DefaultRouter()
# router.register('foods', FoodViewSet)
router.register('payments', PaymentViewSet, base_name='payments')
router.register('users', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_auth.urls")),
    path('auth/registration/', include('rest_auth.registration.urls')),
    path("userEatIn/", view=user_eat_in_view, name="userEatIn"),
    path("userStoreExit/", view=user_store_exit_view, name="userStoreExit"),
]



