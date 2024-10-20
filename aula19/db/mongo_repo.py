from interface import Repositorio

class MongoRepo(Repositorio):

    def insert(self, dado: any) -> None:
        print(f'Inserindo {dado} no repositório MongoDB...')

    def delete(self, dado: any) -> None:
        print(f'Apagando {dado} do repositório MongoDB...')