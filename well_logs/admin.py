from django.contrib import admin
from .models import Operator, Log, Data, Well
from django.utils.translation import gettext as _
from django.db.models import F, Count, Min, Max

# Register your models here.
@admin.register(Log)
class LogAdmin(admin.ModelAdmin):

    search_fields = ['id']
    readonly_fields = ['added','modified']
    fieldsets = [
            ('Well', {'fields':['well',]}),
            ('Log Information', {'fields': [
                ('start_time','finish_time'),
                'operator',
                'comment',
            ]}),
            ('Meta', 
                {'fields':[
                    'added',
                    'modified',
                ]})
    ]

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        queryset = queryset.select_related('site').prefetch_related('data').annotate(
            _data_count=Count('data'),
            _min_depth=Min('data__depth'),
            _max_depth=Max('data__depth'),
            )
        return queryset


    def data_count(self, obj):
        return obj._data_count
    data_count.admin_order_field = '_data_count'
    data_count.short_description = _('count (n)')

    def min_depth(self, obj):
        return obj._min_depth
    min_depth.admin_order_field = '_min_depth'
    min_depth.short_description = _('upper depth (m)')

    def max_depth(self, obj):
        return obj._max_depth
    max_depth.admin_order_field = '_max_depth'
    max_depth.short_description = _('lower depth (m)')

admin.site.register(Operator, admin.ModelAdmin)
admin.site.register(Well, admin.ModelAdmin)