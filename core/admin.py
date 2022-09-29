from django.contrib import admin
from .models import Usuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email','is_superuser', 'is_active', 'is_staff', 'date_joined',]


admin.site.register(Usuario, UsuarioAdmin)    