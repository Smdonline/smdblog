
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, modeladmin_register)
from .models import Work

class WorkAdmin(ModelAdmin):
    model = Work
    menu_label = 'Works'  # ditch this to use verbose_name_plural from model
    # menu_icon = 'pilcrow'  # change as required
    menu_order = 400  # will put in 3rd place (000 being 1st, 100 2nd)
    add_to_settings_menu = False  # or True to add your model to the Settings sub-menu
    exclude_from_explorer = False  # or True to exclude pages of this type from Wagtail's explorer view
    list_display = ('name','email','message','phone','created','read','accepted','working','finished')
    list_filter = ['read','accepted']
    search_fields = ('name','email','phone')
modeladmin_register(WorkAdmin)

