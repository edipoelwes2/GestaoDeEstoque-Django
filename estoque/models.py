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
