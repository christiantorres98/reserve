from django.urls import path, include
from rest_framework.routers import SimpleRouter

from orders.viewsets import OrderModelViewSet

router = SimpleRouter()
router.register('orders', OrderModelViewSet)

app_name = 'orders'
urlpatterns = [
    path('', include(router.urls))
]
