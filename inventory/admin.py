from django.contrib import admin
from .models import Product, Supplier, SaleOrder, StockMovement

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock_quantity', 'supplier')
    search_fields = ('name', 'category')
    list_filter = ('category', 'supplier')

@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address')
    search_fields = ('name', 'email')
    list_filter = ('name',)

@admin.register(SaleOrder)
class SaleOrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'sale_date', 'status')
    search_fields = ('product__name', 'status')
    list_filter = ('status', 'sale_date')

@admin.register(StockMovement)
class StockMovementAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'movement_type', 'movement_date', 'notes')
    search_fields = ('product__name', 'movement_type')
    list_filter = ('movement_type', 'movement_date')
