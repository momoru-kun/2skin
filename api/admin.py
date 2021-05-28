from django.contrib import admin
from .models import Position, Cart, CartPosition, Promocode
# Register your models here.

admin.site.register(Position)
admin.site.register(CartPosition)
admin.site.register(Cart)
admin.site.register(Promocode)