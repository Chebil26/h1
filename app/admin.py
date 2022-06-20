from django.contrib import admin
from django.db.models.fields import AutoFieldMixin
from .models import *
# Register your models here.



class MyModelAdmin(admin.ModelAdmin):
    pass

class TransferAdmin(admin.ModelAdmin):
    search_fields = ('last_name',)
    list_display =  ['first_name', 'last_name','wilaya', 'orginal_uni',  'level', 'spe_choice', 'approved']
    list_filter = ['approved']

admin.site.register(Transfer,TransferAdmin)


