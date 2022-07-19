from django.contrib import admin
from .models import Quantity,Unit, Time, Necessity,Ingredient,QuantityUnitIngredient,QuantityUnitNecessity,Kitchen,Recipe
# Register your models here.
admin.site.register(Recipe)
admin.site.register(Kitchen)
admin.site.register(QuantityUnitNecessity)
admin.site.register(QuantityUnitIngredient)
admin.site.register(Ingredient)
admin.site.register(Necessity)
admin.site.register(Time)
admin.site.register(Unit)
admin.site.register(Quantity)
