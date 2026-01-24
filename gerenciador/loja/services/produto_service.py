from loja.models.produto import Produto

class ProdutoService:
    @staticmethod
    def desativar_produto(produto: Produto):
        produto.ativo = False
        produto.save()

    @staticmethod
    def produtos_visiveis(user):
        qs = Produto.objects.ativos().select_related("marca") # Buscar produtos e marcas com uma consulta somente
        if user.is_staff:
            return qs.filter(usuario=user)
        return qs