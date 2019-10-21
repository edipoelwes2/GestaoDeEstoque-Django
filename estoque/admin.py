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


class PedidoAdmin(admin.ModelAdmin):
    list_filter = ('pagamento', 'marca', 'data_pedido')

    list_display = ('produtos',
                    'data_pedido',
                    'quantidade',
                    'desconto',
                    'total',
                    'pagamento')


admin.site.register(Pedido, PedidoAdmin)