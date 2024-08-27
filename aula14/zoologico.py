from typing import Type

class Animal:

    def comer(self) -> None:
        print('O animal está comendo.')

    def dormir(self) -> None:
        print('O animal está dormindo.')

    def andar(self) -> None:
        print('O animal está andando na jaula.')


class Lobos(Animal):
    
    def __init__(self) -> None:
        super().__init__()

    def uivar(self) -> None:
        print("O lobo está uivando.")


class Aves(Animal):

    def __init__(self) -> None:
        super().__init__()

    def cantar(self) -> None:
        print("A ave está cantando.")

class Pinguim(Aves):

    def __init__(self) -> None:
        super().__init__()

    def escorregar(self) -> None:
        print("O pinguim está escorregando.")
        
    def cantar(self) -> None:
        print("O pinguim está cantando.")

class Falcao(Aves):

    def __init__(self) -> None:
        super().__init__()

    def voar(self) -> None:
        print("O falcão está voando.")

    def cantar(self) -> None:
        print("O falcão está cantando.")

class Pessoa:

    def observar(self, animal: Type[Aves]) -> None:
        animal.cantar()

ruan = Pessoa()
ave = Aves()
pinguim = Pinguim()
falcao = Falcao()
ruan.observar(ave)
ruan.observar(pinguim)
ruan.observar(falcao)
