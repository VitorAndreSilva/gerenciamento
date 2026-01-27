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
    def get_queryset(self):
        return ProdutoService.produtos_visiveis(self.request.user)
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
    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)
    # Deletar
    def perform_destroy(self, instance):
        ProdutoService.desativar_produto(instance)
     