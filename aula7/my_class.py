from typing import Type

class Interruptor:

    def __init__(self, comodo: str) -> None:
        self.__comodo = comodo

    def acender(self) -> None:
        print(f"Acendendo Luzes do(a) {self.__comodo}")
    
    def apagar(self) -> None:
        print(f"Apagando Luzes do(a) {self.__comodo}")


class Pessoa:

    def acender_luz(self, interruptor: Type[Interruptor]):
        interruptor.acender()

    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar()

    def dormir(self) -> None:
        print("Foi dormir")


ruan = Pessoa()
interruptor_quarto = Interruptor('Quarto')
interruptor_cozinha = Interruptor('Cozinha')

ruan.acender_luz(interruptor_quarto)
ruan.apagar_luz(interruptor_cozinha)
ruan.dormir()
