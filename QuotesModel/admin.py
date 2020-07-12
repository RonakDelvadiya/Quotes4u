from django.contrib import admin
from models import *

class DayAdmin(admin.ModelAdmin):
    list_display = ('dayname','dateofday','dayhistory')
    search_fields = ('dayname',)
    
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','occupationid',)
    search_fields = ('name',)

class OccupationAdmin(admin.ModelAdmin):
    list_display = ('occupation',)
    search_fields = ('occupation',)
    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category',)
    search_fields = ('category',)
    
class QuotesAdmin(admin.ModelAdmin):
    list_display = ('quote','authorid','get_category','quotesday',)
    search_fields = ('quote','authorid','get_category','quotesday',)
    list_filter = ('authorid','quotesday',)
    
admin.site.register(Days,DayAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occupation,OccupationAdmin)
admin.site.register(Quotes,QuotesAdmin)



