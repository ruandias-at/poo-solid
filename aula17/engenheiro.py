from interfaces.formas import FormasInterface
from typing import Type

class Engenheiro:
    
    def __init__(self, nome: str) -> None:
        self.__nome = nome

    def medir_perimetro(self, terreno: Type[FormasInterface]) -> None:
        perimetro = terreno.get_perimetro()
        print(f'{self.__nome} mediu o perímetro: {perimetro} m')

    def medir_area(self, terreno: Type[FormasInterface]) -> None:
        area = terreno.get_area()
        print(f'{self.__nome} mediu a área: {area} m²')
