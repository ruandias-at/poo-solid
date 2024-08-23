class PessoaA:

    def se_apresentar(self) -> None:
        print("Olá, sou a pessoa A!")

class PessoaB(PessoaA):

    def __init__(self) -> None:
        super().__init__()
            
    def se_apresentar(self) -> None:
        print('estou alterando esse método')

class PessoaC(PessoaB):

    def __init__(self) -> None:
        super().__init__()

    def se_apresentar(self) -> None:
        print('estou alterando esse método novamente hehe!')

pessoa = PessoaA()
pessoa.se_apresentar()

pessoa2 = PessoaB()
pessoa2.se_apresentar()

pessoa3 = PessoaC()
pessoa3.se_apresentar()
