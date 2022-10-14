from django.contrib import admin
from . models import *

# Register your models here.


class catadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
admin.site.register(categ,catadmin)

class prodadmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}
    list_display=['name','slug','img','price','stock','available']
    list_editable=['price','stock','img','available']
admin.site.register(product,prodadmin)