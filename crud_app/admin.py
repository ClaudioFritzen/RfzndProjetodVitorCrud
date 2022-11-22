from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'f_name', 'l_name', 'cpf', 'age', 'email']
