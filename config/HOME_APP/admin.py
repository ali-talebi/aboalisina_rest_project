from django.contrib import admin
from .models import Banner_Slider , LOGO
# Register your models here.


@admin.register(Banner_Slider)
class Banner_Slider_Admin(admin.ModelAdmin):
    list_display = ['banner_name','created','updated','banner_time']
    search_fields = ['banner_name','created_at','updated_at']
    
@admin.register(LOGO)
class LOGO_Admin(admin.ModelAdmin):
    list_display = ['name',]