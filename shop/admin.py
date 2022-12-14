from django.contrib import admin

# Register your models here.
from.models import OrderUpdate, Orders, product,Contact

admin.site.register(product)
admin.site.register(Contact)
admin.site.register(Orders)
admin.site.register(OrderUpdate)

