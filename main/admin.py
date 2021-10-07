from django.contrib import admin
from .models import*
# Register your models here.
admin.site.register(Contact)
admin.site.register(Comment)
@admin.register(Blog)
class BlogAddmin(admin.ModelAdmin):
	list_display = ['title','date']
	list_display_links = ['title']
	prepopulated_fields = {'slug':('title',)}
@admin.register(Portfolio)
class Portfolio(admin.ModelAdmin):
	list_display = ['title','date']
	list_display_links = ['title']	
	prepopulated_fields = {'slug':('title',)}