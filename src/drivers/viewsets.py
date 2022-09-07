import datetime

from django.db.models import F, Count
from django.db.models.functions import ACos, Cos, Radians, Sin
from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from drivers.models import Driver
from drivers.serializers import DriverModelSerializer, SearchPointSerializer
from orders.models import Order


class DriverModelViewSet(ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverModelSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    http_method_names = ['get']
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ["user__username", "user__first_name"]
    ordering_fields = ["last_update", "-last_update"]

    @action(detail=False, url_path='closest')
    def closest(self, request):
        """Find the closest driver to a reference point in a specific date.
        """

        point = SearchPointSerializer(data=request.data)
        if not point.is_valid():
            return Response(point.errors,
                            status=status.HTTP_400_BAD_REQUEST)

        latitude = request.data['lat']
        longitude = request.data['lng']
        date = request.data['date']
        an_our_before = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ") - datetime.timedelta(hours=24)
        orders = Order.objects.filter(start_date__lte=date, end_date__gte=date)
        query = Driver.objects.filter(last_update__lte=date)
        query = query.exclude(order__in=orders)
        query = query.annotate(
            distance=ACos(
                Cos(
                    Radians(latitude)
                ) * Cos(
                    Radians(F('lat'))
                ) * Cos(
                    Radians(F('lng')) - Radians(longitude)
                ) + Sin(
                    Radians(latitude)
                ) * Sin(Radians(F('lat')))
            ) * 1
        ).order_by('distance')[:1]
        page = self.paginate_queryset(query)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(query, many=True)
        return Response(serializer.data)
