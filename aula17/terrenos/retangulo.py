from interfaces.formas import FormasInterface

class TerrenoRetangular(FormasInterface):

    def __init__(self, largura: float, altura: float) -> None:
        self.__largura = largura
        self.__altura = altura

    def get_perimetro(self):
        perimetro = (self.__altura * 2) + (self.__largura * 2)
        return perimetro
    
    def get_area(self):
        area = self.__largura * self.__altura
        return area
    
    