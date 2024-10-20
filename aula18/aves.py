from interface import AveVoadora, AveTerrestre

class Canario(AveVoadora):

    def comer(self) -> None:
        print('Estou comendo')
        
    def voar(self) -> None:
        print('Estou voando')

    def gritar(self) -> None:
        print('Estou gritando')

class Pinguim(AveTerrestre):

    def comer(self) -> None:
        print('Estou comendo')

    def gritar(self) -> None:
        print('Estou gritando')
