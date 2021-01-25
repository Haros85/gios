from django.contrib import admin
from .models import News, TypeSmi, NewsType, Department, KeyWord, Smi

class TypeSmiAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")

class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")

class DeptAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")

class KeyWordAdmin(admin.ModelAdmin):
    list_display = ("pk", "name")

class SmiAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "url", "type_smi")

class NewsAdmin(admin.ModelAdmin):
    list_display = ("pk", "pub_date", "smi", "name", "url", "display_key", "age", "news_type", "display_ts", "display_dept") 
    search_fields = ("name",)
    list_filter = ("pub_date",) 
    empty_value_display = '-пусто-'

admin.site.register(TypeSmi, TypeSmiAdmin)
admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(Department, DeptAdmin)
admin.site.register(KeyWord, KeyWordAdmin)
admin.site.register(Smi, SmiAdmin)
admin.site.register(News, NewsAdmin)