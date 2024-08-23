from typing import Type

class Animal:

    def comer(self) -> None:
        print('O animal está comendo.')

    def dormir(self) -> None:
        print('O animal está dormindo.')

    def andar(self) -> None:
        print('O animal está andando na jaula.')

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

class Pessoa:

    def observar(self, animal: Type[Aves]) -> None:
        animal.cantar()

roberto = Pessoa()
pinguim = Pinguim()
roberto.observar(pinguim)
