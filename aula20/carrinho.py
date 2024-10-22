from produtos import Produtos
from typing import Type

class CarrinhoDeCompras:

    def __init__ (self) -> None:
        self.__produtos = []

    def add_produto(self, produto: Type[Produtos]) -> None:
        self.__produtos.append(produto)

    def finalizar_compra(self) -> None:
        print(f'Compras finalizadas!')
        for produto in self.__produtos:
            produto.info_prod()
