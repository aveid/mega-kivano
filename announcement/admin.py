from django.contrib import admin

from announcement.models import Item, Recall


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', "price", "created_at", "updated_at",
                    "count", "sub_category", "article"]


admin.site.register(Item, ItemAdmin)


class RecallAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'rate']


admin.site.register(Recall, RecallAdmin)
