class Produtos:

    def __init__ (self, prod_nome: str, prod_valor: int) -> None:
        self.__prod_nome = prod_nome
        self.__prod_valor = prod_valor

    def info_prod(self) -> None:
        print(f'Produto: {self.__prod_nome}, Valor: R${self.__prod_valor},00')
