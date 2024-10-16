from interfaces.formas import FormasInterface

class TerrenoQuadrado(FormasInterface):

    def __init__(self, lado: float) -> None:
        self.lado = lado

    def get_perimetro(self):
        perimetro = self.lado * 4
        return perimetro
    
    def get_area(self):
        area = self.lado ** 2
        return area
    
    