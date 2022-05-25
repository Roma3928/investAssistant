from django.contrib import admin
from .models import Tax


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'tax_rate', 'created_date')
    search_fields = ('state', 'tax_rate')
