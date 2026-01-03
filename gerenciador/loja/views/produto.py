from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from loja.models.produto import Produto
from loja.serializers.produto import ProdutoReadSerializer, ProdutoWriteSerializer
from loja.services.produto_service import ProdutoService
from loja.filters.ProdutoFilter import ProdutoFilter

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.ativos().select_related("marca") # Buscar produtos e marcas com uma consulta somente
    # Serializer
    def get_serializer_class(self): # Definir qual serializer usar
        if self.action in ["list", "retrieve"]:
            return ProdutoReadSerializer # Se o método http direcionar para leitura do produto
        return ProdutoWriteSerializer # Se o método http direcionar para alguma alteração no produto
    # Permissão
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]
    # Filtros
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filerset_class = ProdutoFilter
    ordering_fields = ["preco", "criado_em", "nome", "marca"] # Parâmetros pelo que se pode ordenar
    # Deletar
    def perform_destroy(self, instance):
        ProdutoService.desativar_produto(instance)

from loja.models.produto import Produto
from loja.serializers.produto import ProdutoReadSerializer, ProdutoWriteSerializer
from loja.services.produto_service import ProdutoService
from loja.filters.ProdutoFilter import ProdutoFilter

class ProdutoViewSet(ModelViewSet):
    queryset = Produto.objects.ativos().select_related("marca") # Buscar produtos e marcas com uma consulta somente
    # Serializer
    def get_serializer_class(self): # Definir qual serializer usar
        if self.action in ["list", "retrieve"]:
            return ProdutoReadSerializer # Se o método http direcionar para leitura do produto
        return ProdutoWriteSerializer # Se o método http direcionar para alguma alteração no produto
    # Permissão
    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            return [AllowAny()]
        return [IsAdminUser()]
    # Filtros
    filterset_class = ProdutoFilter
    ordering_fields = ["preco", "criado_em", "nome", "marca"] # Parâmetros pelo que se pode ordenar
    # Deletar
    def perform_destroy(self, instance):
        ProdutoService.desativar_produto(instance)