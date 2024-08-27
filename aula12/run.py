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
        print(f"Estou brincando com o(a) {brinquedo}. rsrs")


class Neta(Filha):

    def __init__(self, endereco: str) -> None:
        super().__init__(endereco)


ana = Mae('Rua de merda')
duda = Filha('Lagoa azul')
duda.brincar('Dildo do Thanos')
print(ana.endereco)
print(duda.endereco)
