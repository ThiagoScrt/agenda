from django.contrib import admin
from core.models import Evento

# Register your models here.

class EveventoAdmin(admin.ModelAdmin):
    list_display = ('id','titulo', 'data_evento', 'data_criacao')
    list_filter = ('usuarios', 'data_evento',)

admin.site.register(Evento, EveventoAdmin)
