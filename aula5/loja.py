class Loja:

    tarifa = 1.03

    def __init__ (self, endereco:str) -> None:
        self.__endereco = endereco
    
    def apresentar_endereco (self) -> None:
        print(self.__endereco)

    @classmethod
    def vender (cls) -> float:
        return 40 * cls.tarifa

    @classmethod
    def alterar_tarifa (cls, nova_tarifa: float) -> None:
        cls.tarifa = nova_tarifa


lojaPraia = Loja('Praia')
lojaCentro = Loja('Centro')

lojaPraia.apresentar_endereco()

print(lojaPraia.vender())
print(lojaCentro.vender())

lojaCentro.alterar_tarifa(1.5)

print(lojaPraia.vender())
print(lojaCentro.vender())
