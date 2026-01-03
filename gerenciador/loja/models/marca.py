from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=25)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    def delete(self, *args, **kwargs):
        self.ativo = False
        self.save()

    def __str__(self):
        return self.nome