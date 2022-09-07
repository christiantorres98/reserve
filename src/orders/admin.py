from django.contrib import admin
from django.utils.safestring import mark_safe

from commons.admin import AuditAdmin
from orders.models import Order


@admin.register(Order)
class OrderAdmin(AuditAdmin):
    list_display = ('driver', 'client', 'start_date', 'end_date', '_start_location', '_destiny_location')
    search_fields = ('id', 'driver__user__username', 'driver__user__first_name', 'driver__user__last_name',
                     'user__username')
    raw_id_fields = ('driver', 'client')

    def _start_location(self, obj):
        html = f'<li>latitud: {obj.start_lat}</li>'
        html += f'<li>longitus: {obj.start_lng}</li>'
        return mark_safe(f'<ul>{html}</ul>')

    _start_location.short_description = 'ubicación inicial'

    def _destiny_location(self, obj):
        html = f'<li>latitud: {obj.destiny_lat}</li>'
        html += f'<li>longitus: {obj.destiny_lng}</li>'
        return mark_safe(f'<ul>{html}</ul>')

    _destiny_location.short_description = 'ubicación destino'
