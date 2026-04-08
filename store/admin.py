from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Category, Product, HeroSlide, Inquiry
from .forms import ProductAdminForm, CategoryAdminForm,HeroSlideAdminForm


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm  # MUHIMU: Inaunganisha JS hapa

    list_display = ['image_preview', 'name', 'slug', 'icon', 'order', 'is_active', 'product_count_display']
    list_editable = ['order', 'is_active']
    prepopulated_fields = {'slug': ('name',)}

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)

        # Kwenye model yako field inaitwa 'image_url'
        if db_field.name == "image_url":
            formfield.widget.attrs.update({
                "role": "uploadcare-uploader",
                "data-public-key": "4c3ba9de492e0e0eaddc",
                "data-images-only": "true",
            })
        return formfield

    def image_preview(self, obj):
        if obj.image_url:
            url = f"https://ucarecdn.com/{obj.image_url}/-/resize/x40/-/format/auto/"
            return mark_safe(f'<img src="{url}" style="max-height:40px; border-radius:4px;" />')
        return "No Image"

    image_preview.short_description = "Preview"

    def product_count_display(self, obj):
        return obj.product_count
    
    product_count_display.short_description = "Products"





@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    form = ProductAdminForm

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
    def formfield_for_dbfield(self, db_field, **kwargs):
            formfield = super().formfield_for_dbfield(db_field, **kwargs)

            # Orodha ya majina ya picha zako zote nne
            image_fields = ["image_url", "image_url_2", "image_url_3", "image_url_4"]

            if db_field.name in image_fields:
                formfield.widget.attrs.update({
                    "role": "uploadcare-uploader",
                    "data-public-key": "4c3ba9de492e0e0eaddc",
                    # Unaweza kuongeza hii ili kuruhusu picha tu
                    "data-images-only": "true",
                })

            return formfield

    def image_preview(self, obj):
        html = '<div style="display: flex; gap: 5px;">'
        
        # Tunachukua picha zote kupitia ile property ya 'images' uliyotengeneza kwenye Model
        picha_zilizopo = obj.images # Hii inarudisha list ya URL zenye data
        
        if picha_zilizopo:
            for url in picha_zilizopo:
                # Tunatumia resize ndogo ili zitoshee kwenye mstari mmoja wa Admin
                cdn_url = f"https://ucarecdn.com/{url}/-/resize/x50/-/format/auto/"
                html += f'<img src="{cdn_url}" style="max-height:50px; border-radius:4px; border:1px solid #ddd;" />'
            
            html += '</div>'
            return mark_safe(html)
        
        return "No Images"

    image_preview.short_description = "Galleru Preview"

# admin.site.register(Product, ProductAdmin)


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    form = HeroSlideAdminForm
    list_display = ['title', 'order', 'is_active']
    list_editable = ['order', 'is_active']

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, **kwargs)

        # Kwenye model yako field inaitwa 'image_url'
        if db_field.name == "image_url":
            formfield.widget.attrs.update({
                "role": "uploadcare-uploader",
                "data-public-key": "4c3ba9de492e0e0eaddc",
                "data-images-only": "true",
            })
        return formfield

    def image_preview(self, obj):
        if obj.image_url:
            url = f"https://ucarecdn.com/{obj.image_url}/-/resize/x40/-/format/auto/"
            return mark_safe(f'<img src="{url}" style="max-height:40px; border-radius:4px;" />')
        return "No Image"

    image_preview.short_description = "Preview"

    def product_count_display(self, obj):
        return obj.product_count
    
    product_count_display.short_description = "Products"


@admin.register(Inquiry)
class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'product', 'created_at', 'is_read']
    list_editable = ['is_read']
    list_filter = ['is_read']
