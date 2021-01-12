from django.contrib import admin
from .models import contacts
# Register your models here.

@admin.register(contacts)
class contactsAdmin(admin.ModelAdmin):
    list_display = ('id','name','created')