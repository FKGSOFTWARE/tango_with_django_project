from django.contrib import admin
from rango.models import Category, Page

# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Update the registration to include this customised interfac
admin.site.register(Category, CategoryAdmin)

@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ("title","category","url")