from django.contrib import admin
from .models import ActiveToken 
# Register your models here.


@admin.register(ActiveToken)
class ActiveToken_Admin(admin.ModelAdmin):
    list_display = ['user','token','created_at']