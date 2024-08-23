class MinhaClasse:

    def __init__ (self, estado: bool) -> None:
        self.estado = estado

    @staticmethod
    def metodo_estatico ():
        print("Estou no meu método estático :)")


obj = MinhaClasse(True)
obj.metodo_estatico()