from django.contrib import admin
from .models import *

admin.site.site_header = 'LittleOneStore'
admin.site.index_title = 'Recursos'
admin.site.site_title = 'littleOne'

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'telefone', 'email')

admin.site.register(Cliente, ClienteAdmin)


class ProdutosAdmin(admin.ModelAdmin):
    list_per_page = 10
    list_filter = ('tipo_Produto', 'marca_produto', 'tamanho',)

    list_display = ('marca_produto',
                    'marca_modelo',
                    'modelo_Produto',
                    'unidades',
                    'tamanho',
                    'estoque',
                    'valor_Entrada',
                    'valor_Saida')

admin.site.register(Produtos, ProdutosAdmin)


class PedidoItensInline(admin.TabularInline):
    model = PedidoItens
    extra = 0


class PedidoAdmin(admin.ModelAdmin):
    inlines = (PedidoItensInline, )
    search_fields = ('data_pedido',)
    list_filter = ('data_pedido', 'pago',)
    list_display = ('id_pedido', 'cliente', 'data_pedido', 'pago',)
    list_display_links = ('cliente',)
    date_hierarchy = 'data_pedido'
    list_per_page = 10

admin.site.register(Pedido, PedidoAdmin)

class PedidoItensAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'produto', 'quantidade', 'desconto', 'subtotal',)
    list_per_page = 10


admin.site.register(PedidoItens, PedidoItensAdmin)