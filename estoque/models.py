from django.db import models

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
    valor_Entrada = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)
    valor_Saida = models.DecimalField(max_digits=5, decimal_places=2, null=False, blank=False)

    def __str__(self):
        return f'{self.marca_produto} | {self.marca_modelo} | {self.modelo_Produto} | {self.unidades} unidades | R$ {self.valor_Saida}'
