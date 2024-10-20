from typing import Type
from db.interface import Repositorio
from db.mongo_repo import MongoRepo
from db.mysql_repo import MySqlRepo

class User:

    def __init__(self, repositorio: Type[Repositorio]) -> None:
        self.__repositorio = repositorio

    def armazenarDados(self, dado: any) -> None:
        self.__repositorio.insert(dado)
        print(f'{dado} adicionado com sucesso!' )

    def removerDado(self, dado: any) -> None:
        self.__repositorio.delete(dado)
        print(f'{dado} removido com sucesso!')

userS = User(MySqlRepo())
userM = User(MongoRepo())
userM.armazenarDados(123)
userS.removerDado('Ruas')
