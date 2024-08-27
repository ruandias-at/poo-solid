from typing import Dict

class Repositorio:

    def select(self, nome: str) -> Dict:
        return {'nome': nome, 'idade':  32}
    
    def insert(self, nome: str, idade: int) -> Dict:
        print(f'Inserindo Dados {nome} e {idade}')
        return {'nome': nome, 'idade':  idade}
