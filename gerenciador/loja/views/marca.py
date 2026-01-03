from rest_framework.viewsets import ModelViewSet
from loja.models.marca import Marca
from loja.serializers.marca import MarcaReadSerializer, MarcaWriteSerializer
from loja.services.marca_service import desativar_marca

class MarcaViewSet(ModelViewSet):
    queryset = Marca.objects.filter(ativo=True)
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return MarcaReadSerializer
        return MarcaWriteSerializer
    def perform_destroy(self, instance):
        desativar_marca(instance)