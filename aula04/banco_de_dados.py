from typing import Type

class Conexao:

    def conectar(self) -> None:
        print('Conectando ao banco de dados')

    def desconectar(self) -> None:
        print('Desconectando do banco de dados...')

class MysqlRepo(Conexao):

    def __init__(self) -> None:
        super().__init__()

    def select(self) -> None:
        self.conectar()
        print('SELECT * FROM table')

class CaboDeUso:

    def buscar(self, db_repo: Type[MysqlRepo]) -> None:
        db_repo.select()
