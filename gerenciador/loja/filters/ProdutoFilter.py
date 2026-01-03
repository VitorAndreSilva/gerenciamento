import django_filters
from loja.models.produto import Produto

class ProdutoFilter(django_filters.FilterSet):
    preco_min = django_filters.NumberFilter(
        field_name="preco", lookup_expr="gte"
    ) 
    preco_max = django_filters.NumberFilter(
        field_name="preco", lookup_expr="lte"
    )
    em_falta = django_filters.BooleanFilter(
        method="filtrar_em_falta"
    )

    def filtrar_em_falta(self, queryset, name, value):
        if value:
            return queryset.filter(quantidade=0)
        return queryset

    class Meta:
        model = Produto
        fields = ["ativo", "tipo", "marca", "quantidade"] # Parâmetros pelo que se pode filtrar