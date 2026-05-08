from django.contrib import admin
from .models import StudentInformation,StudentEducationInformation
# Register your models here.


@admin.register(StudentInformation)
class StudentInformation_Admin(admin.ModelAdmin):
    list_display = ['client','name','family','father_name','mother_name','personal_iranian_id','hbd']
    search_fields = ['name','family','persona_iranian_id','father_name','mother_name']
    
    
    
@admin.register(StudentEducationInformation)
class StudentEducationInformationAdmin(admin.ModelAdmin):
    
    list_display = (
        "client",
        "get_username",
        "get_email",
        "get_first_name",
        "get_last_name",
        "created_at",
    )
    

    search_fields = (
        "client__username",
        "client__email",
        "client__first_name",
        "client__last_name",
    )


    def get_username(self, obj):
        return obj.client.username

    def get_email(self, obj):
        return obj.client.email

    def get_first_name(self, obj):
        return obj.client.first_name

    def get_last_name(self, obj):
        return obj.client.last_name

    get_username.short_description = "Username"
    get_email.short_description = "Email"
    get_first_name.short_description = "First Name"
    get_last_name.short_description = "Last Name"    

    
    
    
    fieldsets = (
        ('اطلاعات پایه', {
            'fields': ('client',)
        }),
        ('مدارک تحصیلی', {
            'fields': (
                'class_1', 'class_2', 'class_3', 'class_4', 
                'class_5', 'class_6', 'class_7', 'class_8', 
                'class_9', 'class_10', 'class_11', 'class_12'
            ),
        }),
    )
    
    readonly_fields = ('created_at',)
    