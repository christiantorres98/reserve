from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from commons.models import Audit


class Driver(Audit):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuario')
    lat = models.IntegerField(
        'latitud',
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        default=0)
    lng = models.IntegerField(
        'longitud',
        validators=[MaxValueValidator(100), MinValueValidator(0)],
        default=0)
    last_update = models.DateTimeField('Ultima actualización', blank=True, null=True)

    class Meta:
        verbose_name = "Conductor"
        verbose_name_plural = "Conductores"

    def __str__(self):
        return self.user.username


class Day(Audit):
    name = models.CharField('Nombre', max_length=124, unique=True)
    num = models.PositiveSmallIntegerField('Número')

    class Meta:
        verbose_name = "Día"
        verbose_name_plural = "Días"

    def __str__(self):
        return self.name


class Schedule(Audit):
    driver = models.ForeignKey(Driver, verbose_name='Conductor', on_delete=models.CASCADE)
    days = models.ManyToManyField(Day)
    start_time = models.TimeField('Hora inicial')
    end_time = models.TimeField('Hora final')

    class Meta:
        verbose_name = 'Horario'
        verbose_name_plural = 'Horarios'

    def __str__(self):
        return f'Horario del conductor: {self.driver}'
