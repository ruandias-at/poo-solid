class Pessoa:

    def __init__ (self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def correr(self) -> None:
        print(f"{self.nome} está correndo")

    def beber(self, bebida: str) -> None:
        if bebida == 'Cerveja':
            self.__apresentar_documento()
            if(self.idade >= 18):
                print(f"{self.nome} está bebendo {bebida}.")
            else:
                print(f"Você é de menor e não pode beber {bebida}.")
        else:
            print(f"{self.nome} está bebendo {bebida}.")

    def __apresentar_documento(self) -> None:
        print(f"CPF de número: {self.__cpf}")

eu = Pessoa('Ruan', 18, '034.929.571-96')
eu.beber('Cerveja')
eu.correr()
