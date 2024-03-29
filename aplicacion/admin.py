from django.contrib import admin
from .models import *

class AlojamientoAdmin(admin.ModelAdmin):
    list_display = ("titulo", "ciudad", "precio")
    list_filter = ("precio",)

admin.site.register(Usuario)
admin.site.register(Alojamiento, AlojamientoAdmin)
admin.site.register(Review)
admin.site.register(Ciudad)
