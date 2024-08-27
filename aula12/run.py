class Mae:

    def __init__(self) -> None:
        self.endereco = 'Rua do Pintão'
        self.sobrenome = "Soares"

    def comer(self) -> None:
        print("Estou comendo(o cu de quem tá lendo)!!!")

    def estudar(self) -> None:
        print("Eu vou te estudar!")


class Filha(Mae):

    def __init__(self) -> None:
        super().__init__()


clara = Filha()
clara.estudar()
