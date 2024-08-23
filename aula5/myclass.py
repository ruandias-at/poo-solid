class MinhaClasse:

    def __init__ (self, estado: bool) -> None:
        self.estado = estado

    def print_estatico(self) -> None:
        print(self.estatico)

    @classmethod
    def mudar_estatico(cls) -> None:
        cls.estatico = 'Programmer'

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
obj1.mudar_estatico()
obj1.print_estatico()
obj2.print_estatico()
