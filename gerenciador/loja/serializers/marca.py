from rest_framework import serializers
from loja.models.marca import Marca

class MarcaReadSerializer(serializers.ModelSerializer):
    total_produtos = serializers.IntegerField(
        source='produtos.count',
        read_only=True
    )
    class Meta:
        model = Marca
        fields = [
            'id',
            'nome',
            'total_produtos'
        ]

class MarcaWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = ["nome"]