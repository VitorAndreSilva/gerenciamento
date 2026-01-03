from django.contrib import admin

from loja.models.produto import Produto
from loja.models.marca import Marca

admin.site.register(Produto)
admin.site.register(Marca)