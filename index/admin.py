from django.contrib import admin
from .models import Campaign, Register

# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
    list_display = (
        'idx', 'name', 'date', 'time', 
        'location', 'description', 'announcer', 'register_num'
    )

class RegisterAdmin(admin.ModelAdmin):
    list_display = (
        'idx', 'user', 'campaign'
    )

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(Register, RegisterAdmin)