class Calculadora:

    def calcular(self, num1: int, op: str, num2: int):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            print("Operação Inválida")

    def __adicionar(self, num1: int, num2: int) -> int:
        return num1 + num2

    def __subtrair(self, num1: int, num2: int) -> int:
        return num1 - num2


minha_calc = Calculadora()
resultado = minha_calc.calcular(32, '+', 3)
print(resultado)
