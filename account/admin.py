from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

# # Register your models here.
# class CustomUserAdmin(UserAdmin):
#     add_form = UserCreationForm  # Ensure this line is present
#     model = CustomUser

# admin.site.register(CustomUser, CustomUserAdmin)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display =  ['username', 'first_name', 'last_name', 'email', 'role', 'questions_list', 'dob', 'photo', 'date_joined']
    list_filter =  ['username', 'first_name', 'last_name', 'email', 'role', 'questions_list', 'dob', 'photo', 'date_joined']
    search_fields = ['username', 'first_name', 'last_name', 'email', 'role', 'questions_list', 'dob', 'photo', 'date_joined']
    date_hierarchy = 'date_joined'
    ordering = ['date_joined', 'role']
    # raw_id_fields = ['username']