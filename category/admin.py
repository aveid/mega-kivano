from django.contrib import admin

from category.models import Category, SubCategory


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]


admin.site.register(Category, CategoryAdmin)


class SubCategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category']


admin.site.register(SubCategory, SubCategoryAdmin)
