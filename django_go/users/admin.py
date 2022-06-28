from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserChangeForm, CustomUserCreationForm

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm

    add_fieldsets = (
        *UserAdmin.add_fieldsets,('Custom fields',{'fields': (
                    'gender',
                    'age')}))

    fieldsets = (
        *UserAdmin.fieldsets,('Custom fields',{'fields': (
                    'gender',
                    'age')}))




