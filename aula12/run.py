class Mae:

    def __init__(self, endereco: str) -> None:
        self.endereco = endereco
        self.sobrenome = "Soares"

    def comer(self) -> None:
        print("Estou comendo(o cu de quem tá lendo)!!!")

    def estudar(self) -> None:
        print("Eu vou te estudar!")


class Filha(Mae):

    def __init__(self, endereco: str) -> None:
        super().__init__(endereco)


    def brincar(self, brinquedo: str) -> None:
        print(f"Estou brincando com {brinquedo}. rsrs")

clara = Filha('Rua das merdinhas')
clara.estudar()
print(clara.endereco)
clara.brincar('Dildo')