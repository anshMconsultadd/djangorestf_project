from django.contrib import admin
from .models import Room, Booking  # import your models

# Register your models here
admin.site.register(Room)
admin.site.register(Booking)