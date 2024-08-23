class Pessoa:

    def __init__ (self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self) -> None:
        print(f"{self.nome} está correndo")

    def beber(self, bebida: str) -> None:
        print(f"{self.nome} está bebendo {bebida}")

    def _apresentar_documento(self) -> None:
        print(f"CPF de número: {self.__cpf}")

eu = Pessoa('Ruan', 18, '034.929.571-96')
eu._apresentar_documento()
eu.beber('Vodka')
eu.correr()
print(eu.idade)