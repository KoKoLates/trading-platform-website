from django.contrib import admin
from .models import Item, Love

# Register your models here.
class ItemAdmin(admin.ModelAdmin):
    list_display = ('idx', 'user', 'name', 'price', 'quantity', 'category', 'transaction_type', 'transaction_location', 'condition', 'image')

class LoveAdmin(admin.ModelAdmin):
    list_display = ('user', 'item')

admin.site.register(Item, ItemAdmin)
admin.site.register(Love, LoveAdmin)
