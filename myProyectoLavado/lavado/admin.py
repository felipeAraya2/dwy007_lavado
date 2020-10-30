from django.contrib import admin
from .models import SliderIndex, Galeria, MisionyVision,Producto

# Register your models here.
class SliderIndexAdmin(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields=['ident']
    list_per_page = 10

class GaleriaAdmin(admin.ModelAdmin):
    list_display=['ident','imagen']
    search_fields=['ident']
    list_per_page = 10

class MisionAdmin(admin.ModelAdmin):
    list_display=['ident','mision','misionImg','vision','visionImg','quienes','quienesImg']
    list_per_page = 10

class ProductoAdmin(admin.ModelAdmin):
    list_display=['nombre','precio','descripcion','stock']
    search_fields=['nombre']
    list_per_page = 10
admin.site.register(SliderIndex, SliderIndexAdmin)
admin.site.register(Galeria, GaleriaAdmin)
admin.site.register(MisionyVision,MisionAdmin)
admin.site.register(Producto,ProductoAdmin)

