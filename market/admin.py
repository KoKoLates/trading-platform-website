from django.contrib import admin
from .models import Item

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('idx', 'user', 'name', 'price', 'quantity', 'category', 'transaction_type', 'transaction_location', 'condition', 'image')

admin.site.register(Item, ItemAdmin)
