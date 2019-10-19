from django.contrib import admin
from .models import *

admin.site.site_header = 'LittleOneStore'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'littleOne'

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email')

admin.site.register(Cliente, ClienteAdmin)