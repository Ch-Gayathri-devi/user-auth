from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Doctor

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_patient', 'is_doctor')
    list_filter = ('is_patient', 'is_doctor', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'profile_picture')}),
        ('Address', {'fields': ('address_line1', 'city', 'state', 'pincode')}),
        ('User Type', {'fields': ('is_patient', 'is_doctor')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

class PatientAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email')
    search_fields = ('user__username', 'user__email')
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_email')
    search_fields = ('user__username', 'user__email')
    
    def get_email(self, obj):
        return obj.user.email
    get_email.short_description = 'Email'

admin.site.register(User, CustomUserAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)

# Register your models here.
