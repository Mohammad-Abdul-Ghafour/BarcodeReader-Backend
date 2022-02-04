from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm

class AccountAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'email', 'date_joined',
                    'last_login', 'is_staff','is_superuser')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')
    list_filter = ()


    fieldsets = UserAdmin.fieldsets + (
        (('Permissions'), {
            'fields': ('role',),
        }),
    )


admin.site.register(CustomUser,AccountAdmin)
