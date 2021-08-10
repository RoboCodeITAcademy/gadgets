from django.contrib import admin
from .models import Category,Tag,Gadget
from django.utils.html import mark_safe

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    prepopulated_fields = {'slug':('name',)}

@admin.register(Gadget)
class GadgetAdmin(admin.ModelAdmin):
    list_display = ['get_image','title','category', 'file_format']
    list_display_links = ['title']
    prepopulated_fields = {'slug':('title',)}
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f"<img src='{obj.image.url}' width='60' height='60'>")

    get_image.short_description = 'Gadget image'