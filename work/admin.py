from django.contrib import admin
from .models import Work
# Register your models here.
@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ('name','email','message','phone','created','read','accepted','working','finished')
    sort_by = ('-created','read')
    list_filter = ['read','accepted']
    search_fields = ('name','email','phone')
