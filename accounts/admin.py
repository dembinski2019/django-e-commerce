from django.contrib import admin
from .forms import UserAdminCreationForm,UserAdminForm
from .models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin



class UserAdmin(BaseUserAdmin):
    
    add_form = UserAdminCreationForm
    add_fieldsets = (
        (None,{
            'fields': ('username','email','password1','password2')
        }),
    )
    form = UserAdminForm
    fieldsets = (
        (None,{
            'fields': ('username', 'email')
        }),
        ('Informações Básicas',{
            'fields':('name','last_login')
        }),
        ('Permissões',{
            'fields':(
                'is_active','is_staff','is_superuser','groups',
                'user_permissions'
            )
        }),
        
    )
    list_display = ['username','name', 'email', 'is_active','is_staff', 'date_joined']


admin.site.register(User,UserAdmin)