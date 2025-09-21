from django.contrib import admin
from .models import User

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['guid', 'created_at', 'updated_at']
    readonly_fields = ['guid', 'created_at', 'updated_at']
    search_fields = ['guid']