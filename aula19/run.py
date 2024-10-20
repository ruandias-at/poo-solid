from typing import Type
from db.mysql_repo import MySqlRepo

class User:

    def __init__(self, repositorio: Type[MySqlRepo]) -> None:
        self.__repositorio = repositorio

    def armazenarDados(self, dado: any) -> None:
        self.__repositorio.insert(dado)
        print(f'{dado} adicionado com sucesso!' )

    def removerDado(self, dado: any) -> None:
        self.__repositorio.delete(dado)
        print(f'{dado} removido com sucesso!')

mysql1 = MySqlRepo()
ruan = User(mysql1)
ruan.armazenarDados('Ruan')
ruan.armazenarDados(True)
ruan.armazenarDados(18)
ruan.removerDado('Ruan')