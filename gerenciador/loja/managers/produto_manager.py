from django.db import models

class ProdutoQueryset(models.QuerySet): # QuerySet customizado que permite acesso ao banco com os filtros
    def ativos(self):
        return self.filter(ativo=True)
    
    def inativos(self):
        return self.filter(ativo=False)
    
class ProdutoManager(models.Manager):
    def get_queryset(self):
        return ProdutoQueryset(self.model, self._db) # Permite o uso do QuerySet customizado
    
    def ativos(self):
        return self.get_queryset().ativos()
    
    def inativos(self):
        return self.get_queryset().inativos()