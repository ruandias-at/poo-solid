
class AbstractClass:

    def __init__(self):
        self.atributo = 'Olá Mundo!'

    def metodo(self, elemento: str) -> None:
        print(elemento)

    def metodo_abstrato(self) -> None:
        pass
