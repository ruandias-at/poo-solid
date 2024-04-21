from typing import Dict
from models import Insersor, Repositorio

class RepositorioFaker(Repositorio):

    def __init__(self) -> None:
        super().__init__()

    def select(self, name: int) -> None:
        return None

repo = RepositorioFaker()
insersor = Insersor(repo)

data = insersor.inserir_dado('Lhama', 26)
print(data)
