from django.contrib import admin
from .models import Post,Post_Category
# Register your models here.

@admin.register(Post_Category)
class Post_Category_Admin(admin.ModelAdmin):
    list_display = ['post_category_name']
    



@admin.register(Post)
class Post_Admin(admin.ModelAdmin):
    list_display = ['post_name','created_at','updated_at']
    search_fields = ['post_name','category']
    