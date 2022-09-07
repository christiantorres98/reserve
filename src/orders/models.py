import datetime

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from commons.models import Audit


class Order(Audit):
    driver = models.ForeignKey('drivers.Driver', verbose_name='Conductor', on_delete=models.CASCADE)
    client = models.ForeignKey(User, verbose_name='Cliente', on_delete=models.CASCADE)
    start_date = models.DateTimeField('Fecha inicial')
    end_date = models.DateTimeField('Fecha final', blank=True)
    start_lat = models.IntegerField('latitud inicial', validators=[MaxValueValidator(100), MinValueValidator(0)])
    start_lng = models.IntegerField('longitud inicial', validators=[MaxValueValidator(100), MinValueValidator(0)])
    destiny_lat = models.IntegerField('latitud destino', validators=[MaxValueValidator(100), MinValueValidator(0)])
    destiny_lng = models.IntegerField('longitud destino', validators=[MaxValueValidator(100), MinValueValidator(0)])

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return f'Pedido #{self.id}'

    def save(self, *args, **kwargs):
        self.end_date = self.start_date + datetime.timedelta(hours=1)
        super().save()
