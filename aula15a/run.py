class PessoaA:

    def se_apresentar(self) -> None:
        print("Olá, sou a pessoa A!")

class PessoaB(PessoaA):

    def __init__(self) -> None:
        super().__init__()
            
    def se_apresentar(self) -> None:
        print('estou alterando esse método')


pessoa1 = PessoaA()
pessoa1.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()
