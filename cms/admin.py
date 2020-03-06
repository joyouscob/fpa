from django.contrib import admin
# Register your models here.
from .models import Page, Post, Setting, Menu, Submenu, Stories


#FOR PREPOPULATING SLUG in the admin
class PageAdmin(admin.ModelAdmin):
    # list_display = ('title', 'body',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Page),
admin.site.register(Post),
admin.site.register(Setting),
admin.site.register(Menu),
admin.site.register(Submenu)
