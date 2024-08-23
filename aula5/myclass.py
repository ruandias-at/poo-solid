class MinhaClasse:

    def __init__ (self, estado: bool) -> None:
        self.estado = estado
        self.estatico = 'Lhama'

    def print_estatico(self) -> None:
        print(self.estatico)

    def mudar_estatico(self) -> None:
        self.estatico = 'Programmer'

obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
obj1.mudar_estatico()
obj1.print_estatico()
print(MinhaClasse.estatico)