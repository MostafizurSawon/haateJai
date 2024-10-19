from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Cart)
admin.site.register(models.CartItem)
admin.site.register(models.Orders)
admin.site.register(models.OrderItem)
admin.site.register(models.UserAccount)
admin.site.register(models.UserSocialAccount)