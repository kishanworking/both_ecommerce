from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Account 

# Register your models here.



# this will be shown on database names
class AccountAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'date_joined', 'is_active')

    # for link on first_name ... it is for database
    list_display_links = ('email','first_name','last_name')

    readonly_fields = ('last_login', 'date_joined')

    # show in decending orders
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    # for password read only 
    fieldsets = ()


admin.site.register(Account, AccountAdmin)