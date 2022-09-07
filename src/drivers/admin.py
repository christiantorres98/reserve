from django.contrib import admin
from django.utils.safestring import mark_safe

from commons.admin import AuditAdmin
from drivers.models import Driver, Day, Schedule


@admin.register(Driver)
class DriverAdmin(AuditAdmin):
    list_display = ('user', 'lat', 'lng', 'last_update')
    list_display_links = ('user', 'lat', 'lng', 'last_update')
    list_filter = ('last_update',)
    search_fields = ('user__username', 'user__first_name', 'user__last_name')
    raw_id_fields = ('user',)


@admin.register(Day)
class DayAdmin(AuditAdmin):
    list_display = ('name', 'num')
    list_display_links = ('name', 'num')


@admin.register(Schedule)
class ScheduleAdmin(AuditAdmin):
    list_display = ('driver', '_get_days', 'start_time', 'end_time')
    list_display_links = ('driver', '_get_days', 'start_time', 'end_time')
    list_filter = ('driver', 'days')
    search_fields = ('driver__user__username', 'driver__user__first_name', 'driver__user__last_name')
    raw_id_fields = ('driver',)

    def _get_days(self, obj):
        days = obj.days.all()
        html = ""
        for day in days:
            html += f'<li>{day.name}</li>'
        return mark_safe(f'<ul>{html}</ul>')

    _get_days.short_description = 'Días'
