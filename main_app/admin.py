from django.contrib import admin
from .models import Farmer, Processor, Distributor, Consumer, Product, Order

@admin.register(Farmer)
class FarmerAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

@admin.register(Processor)
class ProcessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'process_type')
    search_fields = ('name', 'process_type')

@admin.register(Distributor)
class DistributorAdmin(admin.ModelAdmin):
    list_display = ('name', 'region')
    search_fields = ('name', 'region')

@admin.register(Consumer)
class ConsumerAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')
    search_fields = ('name', 'email')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_stakeholder')
    search_fields = ('name',)
    list_filter = ('farmer', 'processor', 'distributor')

    def get_stakeholder(self, obj):
        """Return the stakeholder (farmer, processor, or distributor) associated with the product."""
        if obj.farmer:
            return f"Farmer: {obj.farmer.name}"
        elif obj.processor:
            return f"Processor: {obj.processor.name}"
        elif obj.distributor:
            return f"Distributor: {obj.distributor.name}"
        return "No stakeholder"
    
    get_stakeholder.short_description = 'Stakeholder'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('consumer', 'product', 'quantity', 'payment_method', 'status', 'ordered_on')
    search_fields = ('consumer__name', 'product__name')
    list_filter = ('payment_method', 'status', 'ordered_on')
    ordering = ('-ordered_on',)  # Orders by most recent


