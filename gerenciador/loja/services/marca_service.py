from loja.models.marca import Marca
def desativar_marca(marca: Marca):
    if marca.produtos.filter(ativo=True).exists():
        raise ValueError("Marca possui produtos ativos")
    marca.ativo = False
    marca.save()