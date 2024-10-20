from .interface import Repositorio

class MySqlRepo(Repositorio):

    def insert(self, dado: any) -> None:
        print(f'Inserindo {dado} no repositório MySql...')

    def delete(self, dado: any) -> None:
        print(f'Apagando {dado} do repositório MySql...')