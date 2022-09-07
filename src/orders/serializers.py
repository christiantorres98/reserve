from django.core.exceptions import ValidationError, FieldError
from rest_framework import serializers
from rest_framework.generics import get_object_or_404

from drivers.models import Schedule, Driver
from drivers.serializers import DriverModelSerializer
from orders.models import Order


class OrderModelSerializer(serializers.ModelSerializer):
    # driver = DriverModelSerializer(read_only=True)
    class Meta:
        model = Order
        fields = ('id', 'driver', 'client', 'start_date', 'end_date', 'start_lat', 'start_lng', 'destiny_lat',
                  'destiny_lng')
        read_only_fields = ('end_date',)
        extra_kwargs = {'start_date': {'format': "%Y-%m-%dT%H:%M:%S.%fZ"},
                        'end_date': {'format': "%Y-%m-%dT%H:%M:%S.%fZ"}}

    def validate(self, validated_data):
        instance = Order(**validated_data)
        try:
            instance.clean()
        except ValidationError as e:
            raise serializers.ValidationError(e.args[0])
        return validated_data
