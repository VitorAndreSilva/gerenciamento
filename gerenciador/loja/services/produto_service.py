from loja.models.produto import Produto

class ProdutoService:
    @staticmethod
    def desativar_produto(produto: Produto):
        produto.ativo = False
        produto.save()