from django.contrib import admin

# Register your models here.
from DJangoApp.models import Tours, Kontakt, FavTours

admin.site.register(Tours)
admin.site.register(Kontakt)
admin.site.register(FavTours)