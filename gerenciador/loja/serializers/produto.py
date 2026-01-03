from rest_framework import serializers
from loja.models.produto import Produto

class ProdutoReadSerializer(serializers.ModelSerializer):
    nome_marca = serializers.CharField( # a variável nome_marca serve para lermos diretamente o nome da marca ao acessar um produto, ao invés de lermos o id da mesma
        source="marca.nome",
        read_only=True # Disponível somente ao ler o produto, não ao escrever
    )

    class Meta:
        model = Produto
        fields = [
            "nome",
            "nome_marca",
            "tipo",
            "capacidade",
            "preco",
            "quantidade",
            "valor_total"
        ]

class ProdutoWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = [
            "nome",
            "marca",
            "tipo",
            "capacidade",
            "preco",
            "quantidade"
        ]
    # Validações dizem respeito a erros nas entradas dos dados, por isso, ficam no serializers
    def validate_nome(self, value): # validações sempre ficam no serializer
        if len(value) < 2:
            raise serializers.ValidationError("O nome é curto demais")
        return value
    
    def validate_preco(self, value):
        if value <= 0:
            raise serializers.ValidationError("O valor deve ser maior do que zero")
        return value
    
    def validate_quantidade(self, value):
        if value < 0:
            raise serializers.ValidationError("A quantidade não pode ser negativa")
        return value