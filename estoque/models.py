from django.db import models
from django.utils import timezone

class Cliente(models.Model):
    class Meta:
        verbose_name_plural = 'clientes'
        verbose_name = 'cliente'

    SEXO_CHOICES = (
        ("F", "Feminino"),
        ("M", "Masculino"),
    )

    nome = models.CharField(max_length=100, null=False, blank=False)
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=True, blank=True)
    telefone = models.CharField(max_length=11)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES, blank=False, null=False)

    def __str__(self):
        return self.nome


class Produtos(models.Model):
    class Meta:
        verbose_name_plural = 'produtos'

    PRODUTO_CHOICES = (
        ("Fralda", "Fralda"),
        ("Lenço", "Lenço"),
    )
    TAMANHO_CHOICES = (
        ("LN", "Lenço"),
        ("RN", "RN"),
        ("P", "P"),
        ("M", "M"),
        ("G", "G"),
        ("XG", "XG"),
        ("XXG", "XXG"),
        ("GRA", "Grandinhos"),
    )
    MARCA_CHOICES = (
        ("MamyPoko", "MamyPoko"),
        ("Huggies", "Huggies"),
        ("Pampers", "Pampers"),
        ("Babysec", "Babysec"),
        ("PomPom", "PomPom"),
        ("Cremer", "Cremer"),
        ("Looney Tunes", "Looney Tunes"),
        ("Scooby-Doo", "Scooby-Doo"),
        ("Hipopó", "Hipopó"),
        ("Johnson's", "Johnson's"),
    )

    tipo_Produto = models.CharField(max_length=6, choices=PRODUTO_CHOICES, null=False, blank=False)
    marca_produto = models.CharField(max_length=12, choices=MARCA_CHOICES, null=False, blank=False)
    marca_modelo = models.CharField(max_length=50, null=False, blank=False)
    modelo_Produto = models.CharField(max_length=50, null=False, blank=False)
    unidades = models.PositiveIntegerField()
    tamanho = models.CharField(max_length=3, choices=TAMANHO_CHOICES, null=False, blank=False)
    estoque = models.PositiveIntegerField()
    valor_Entrada = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    valor_Saida = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return '{} | {} | {} | {} unidades | R$ {}'.format(self.marca_produto, self.marca_modelo, self.modelo_Produto, self.unidades, self.valor_Saida)
        #return f'{self.marca_produto} | {self.marca_modelo} | {self.modelo_Produto} | {self.unidades} unidades | R$ {self.valor_Saida}'


class Pedido(models.Model):
    CONTAS = [
        ("NU", "Nubank"),
        ("BB", "Banco do Brasil"),
        ("SP", "Safrapay"),
        ("MP", "Mercado Pago"),
        ("JN", "Jessianne"),
        ("JK", "Jessica")
    ]

    MARCA = (
        ("Mam", "MamyPoko"),
        ("Hug", "Huggies"),
        ("Pam", "Pampers"),
        ("Bab", "Babysec"),
        ("Pom", "PomPom"),
        ("Cre", "Cremer"),
        ("Loo", "Looney Tunes"),
        ("Sco", "Scooby-Doo"),
        ("Hip", "Hipopó"),
        ("Joh", "Johnson's"),
    )
    class Meta:
        verbose_name_plural = 'pedidos'

    def __str__(self):
        return str(self.produtos)

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produtos = models.ForeignKey(Produtos, on_delete=models.CASCADE)
    marca = models.CharField(max_length=3, choices=MARCA, null=False, blank=False)
    conta = models.CharField(max_length=2, choices=CONTAS, null=False, blank=False)
    data_pedido = models.DateField(default=timezone.now)
    quantidade = models.PositiveIntegerField(default=1)
    desconto = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    descricao = models.TextField(null=True, blank=True)


    def total(self):
        return (self.quantidade * self.produtos.valor_Saida) - self.desconto
    total = property(total)
    pagamento = models.BooleanField(default=True)

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        # Salve os dados
        self.produtos.estoque -= self.quantidade
        self.produtos.save()
        super(Pedido, self).save(force_insert, force_update, *args, **kwargs)

