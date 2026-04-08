from django.contrib import admin
from .models import Category, Product, HeroSlide, Inquiry


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'icon', 'order', 'is_active', 'product_count']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'is_featured', 'is_active', 'in_stock', 'created_at']
    list_filter = ['category', 'is_active', 'is_featured', 'in_stock']
    list_editable = ['is_featured', 'is_active', 'in_stock']
    search_fields = ['name', 'description']
    prepopulated_fields = {'slug': ('name',)}
    fieldsets = (
        ('Basic Info', {'fields': ('category', 'name', 'slug', 'description', 'tags')}),
        ('Pricing', {'fields': ('price', 'old_price', 'condition')}),
        ('Images (Uploadcare CDN URLs)', {'fields': ('image_url', 'image_url_2', 'image_url_3', 'image_url_4')}),
        ('Status', {'fields': ('is_active', 'is_featured', 'in_stock', 'stock_qty')}),
    )


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'product', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
