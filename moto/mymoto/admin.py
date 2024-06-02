from django.contrib import admin
from .models import Brands, Bikes, cars,UserProfile,User,deal
# Register your models here.
admin.site.register(Brands)
admin.site.register(Bikes)
admin.site.register(cars)
admin.site.register(UserProfile)
admin.site.register(deal)