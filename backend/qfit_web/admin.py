from django.contrib import admin
from .models import Data
from .models import Feature
# Register your models here.


class DataAdmin(admin.ModelAdmin):
    list_display = ('title',)

class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'values', 'data')

# Register your models here.

admin.site.register(Data, DataAdmin)
admin.site.register(Feature, FeatureAdmin)