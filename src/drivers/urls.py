from django.urls import path, include
from rest_framework.routers import SimpleRouter

from drivers.viewsets import DriverModelViewSet

router = SimpleRouter()
router.register('drivers', DriverModelViewSet)

app_name = 'drivers'
urlpatterns = [
    path('', include(router.urls))
]
