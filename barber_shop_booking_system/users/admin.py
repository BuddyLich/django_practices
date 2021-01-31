from django.contrib import admin
from .models import User, CustomerInfo, BarberInfo


admin.site.register(User)
admin.site.register(CustomerInfo)
admin.site.register(BarberInfo)
