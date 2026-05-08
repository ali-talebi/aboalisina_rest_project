from django.contrib import admin
from .models import School_Comments 
# Register your models here.


@admin.register(School_Comments)
class School_Comments_Admin(admin.ModelAdmin):
    list_display = ['commenter_name','created_at','updated_at']
    search_fields = ['commenter_name']