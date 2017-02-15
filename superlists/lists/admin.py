# -*- coding:utf-8 -*-

from django.contrib import admin
from .models import List, Item

class ListAdmin(admin.ModelAdmin):
    list_display = ('id',)

class ItemAdmin(admin.ModelAdmin):
    list_display = ('text', 'list')

admin.site.register(List, ListAdmin)
admin.site.register(Item, ItemAdmin)
