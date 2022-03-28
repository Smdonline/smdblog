from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from taggit.models import Tag
from django.contrib import admin


class TagAdmin(ModelAdmin):
    model = Tag
    menu_label = 'Tags'  # ditch this to use verbose_name_plural from model
    # menu_icon = 'pilcrow'  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('slug','name_en','name_it')
    list_filter = ('name_en','name_it')
    search_fields = ('name_en','name_it')
modeladmin_register(TagAdmin)
