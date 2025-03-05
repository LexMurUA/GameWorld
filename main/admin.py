from django.contrib import admin
from django.utils.html import format_html
from .models import *

class AdvertisingImageInline(admin.TabularInline):
    model = AdvertisingImage
    can_delete = True
    max_num = 1
    readonly_fields = ['image_preview']
    ordering = ['id']
    
    def image_preview(self, obj):
        if obj and obj.image:
            return format_html('<img src="{}" style="width:100px;height:100px">', obj.image.url)
        return "Немає зображення"

    image_preview.short_description = 'Превью'

@admin.register(Advertising)
class AdvertisingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'link', 'image_preview']
    inlines = [AdvertisingImageInline]

    def image_preview(self, obj):
        if hasattr(obj, 'adv_image') and obj.adv_image.image:
            return format_html('<img src="{}" style="width:100px;height:100px">', obj.adv_image.image.url)
        return "Немає зображення"

    image_preview.short_description = 'Зображення'


@admin.register(Adress)
class AdressAdmin(admin.ModelAdmin):
    list_display = ('adress_text', 'link')
    search_fields = ('adress_text',)

@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('text_about',)