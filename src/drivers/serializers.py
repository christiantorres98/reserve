from django.core.validators import MaxValueValidator, MinValueValidator
from rest_framework import serializers

from drivers.models import Driver, Day, Schedule
from users.serializers import UserModelSerializer


class DriverModelSerializer(serializers.ModelSerializer):
    user = UserModelSerializer()

    class Meta:
        model = Driver
        fields = ('id', 'user', 'lat', 'lng', 'last_update')
        extra_kwargs = {'last_update': {'format': "%Y-%m-%dT%H:%M:%S.%fZ"}}


class DayModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Day
        fields = ('id', 'name', 'num')


class ScheduleModelSerializer(serializers.ModelSerializer):
    day = DayModelSerializer(many=True, read_only=True)

    class Meta:
        model = Schedule
        fields = ('id', 'driver', 'day', 'start_time', 'end_time')


class SearchPointSerializer(serializers.Serializer):
    lat = serializers.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    lng = serializers.IntegerField(validators=[MaxValueValidator(100), MinValueValidator(0)])
    date = serializers.DateTimeField(
        format="%Y-%m-%dT%H:%M:%S.%fZ",
        input_formats=["%Y-%m-%dT%H:%M:%S.%fZ"])
