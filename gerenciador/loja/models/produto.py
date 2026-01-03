from django.db import models
from loja.models.marca import Marca
from loja.managers.produto_manager import ProdutoManager

class Produto(models.Model):
    class TypeChoices(models.TextChoices):
        DESODORANTE = "Desodorante"
        COLONIA = "Colônia"
        BODY_SPLASH = "Body splash"
        SABONETE = "Sabonete"
        ESFOLIANTE = "Esfoliante"
        OLEO_CORPORAL = "Óleo corporal"
        HIDRATANTE = "Hidratante"
        PROTECAO_SOLAR = "Proteção solar"
        ALCOOL_GEL = "Álcool em gel"
        SHAMPOO = "Shampoo"
        CONDICIONADOR = "Condicionador"
        MASCARA = "Máscara de tratamento"
        FINALIZADOR = "Finalizador"
    nome = models.CharField(max_length=100)
    tipo = models.CharField(choices=TypeChoices, max_length=35)
    capacidade = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.IntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT, related_name="produtos")
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    objects = ProdutoManager()

    def save(self, *args, **kwargs): # Sobrescrições de métodos (save, delete, etc) são usadas nas models quando independem de http ou entradas, sendo válidas para todos os lugares onde forem chamados (API, admin, etc)
        if self.quantidade == 0:
            self.ativo = False
        return super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.ativo = False
        self.save()

    @property
    def valor_total(self):
        return self.preco * self.quantidade

    def __str__(self):
        return f'{self.nome} {self.tipo} {self.capacidade}ml'