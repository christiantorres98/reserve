from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated

from orders.models import Order
from orders.serializers import OrderModelSerializer


class OrderModelViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    http_method_names = ['post', 'get']
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    ordering_fields = ["start_date", "-start_date", "start_date__time", "-start_date__time"]
    filter_fields = {
        "driver__id": ["exact"],
        "start_date": ["exact", "date"],
    }
