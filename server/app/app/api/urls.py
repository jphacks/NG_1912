from django.urls import path, include
from rest_framework import routers
from app.api.foods.views import FoodViewSet
from app.api.payments.views import PaymentViewSet
from app.api.users.views import UserViewSet

app_name = "api"

router = routers.DefaultRouter()
router.register('foods', FoodViewSet)
router.register('payments', PaymentViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("auth/", include("rest_auth.urls")),
    path('auth/registration/', include('rest_auth.registration.urls')),
]



