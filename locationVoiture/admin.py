from django.contrib import admin
from locationVoiture.models import Client, Vehicule, Reservation, Blog, Contact


# Register your models here.

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    pass


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    pass


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass


@admin.register(Contact)
class ReservationAdmin(admin.ModelAdmin):
    pass
