from django.contrib import admin

from .models import (Corrente,
                     )

class CorrenteAdmin(admin.ModelAdmin):

    list_display = ('titulo',
                    'disponivel',
                    )

    list_filter = ('titulo',
                   'disponivel',
                   )

    search_fields = ('titulo',
                     'disponivel',
                     'corrente',
                    )

    class Meta:
        model = Corrente

admin.site.register(Corrente, CorrenteAdmin)