from django.contrib import admin

from main.models import Category, Dish, Review, Order

admin.site.site_header = 'TerraSilvita'

admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(Order)
