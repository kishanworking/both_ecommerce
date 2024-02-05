from django.contrib import admin
from .models import Category



# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    # for auto taing in slug 
    prepopulated_fields = {'slug': ('category_name',)}

    # name showing on database 
    list_display = ('category_name','slug')
    

    
admin.site.register(Category, CategoryAdmin)