from django.contrib import admin
from .models import *
from django.utils.html import format_html

# Register your models here.
admin.site.register([Vendor, Genre, Category, Tag, ProductImage])

class ProductImageTabular(admin.TabularInline):
    model = ProductImage
    extra = 3
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        return format_html (f'<img style="width:50px;height=50px" src="{obj.image.url}">')

    image_preview.short_description = 'Зображення'
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'image_preview', 'code', 'name', 'product_category', 'sale_price', 'price', 'updated_at', 'tags_preview' ] #відображення панель
    readonly_fields = ['created_at'] 
    list_display_links = ['code', 'name']
    ordering = ['sale_price', 'price', 'created_at'] 
    list_filter = ['tags', 'product_category', 'vendor']
    list_editable = ['sale_price', 'price', 'product_category' ]
    list_per_page = 20
    filter_horizontal = ['tags']
    search_fields = ['code', 'name']
    inlines = [ProductImageTabular]
    actions = ['up_price', 'up_sale_price']

    def image_preview(self, obj):
        all_images = obj.images.all()
        if len(all_images):
            return format_html (f'<img style="width:50px;height=50px" src="{all_images.first().image.url}">')

        else:
            return format_html ("<p style='color:red'>Зображення не знайдено</p>")

    image_preview.short_description = 'Зображення'

    def up_price(self, request, queryset):
        for product in queryset:
            product.price += 10
            product.save()
    
    up_price.short_description = 'Збільшення ціни на 10'

    def up_sale_price(self, request, queryset):
        for product in queryset:
            product.sale_price += 10
            product.save()
            

    up_sale_price.short_description = 'Збільшення акційної ціни на 10'

    def tags_preview(self, obj):
        tags = obj.tags.all()
        if len(tags):
            result_str = ''.join([f'<li>{tag.name}</li>' for tag in tags])
            return format_html(f'<ul>{result_str}</ul>')
        else:
            return format_html("<p style='color:red'>Теги не знайдено</p>")
        
    tags_preview.short_description = 'Теги'


