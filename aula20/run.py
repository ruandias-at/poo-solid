from produtos import Produtos
from carrinho import CarrinhoDeCompras

car = CarrinhoDeCompras()
monitor = Produtos('Monitor AOC' , 450)
cerveja = Produtos('Stella Artois', 6)
tv = Produtos('Samsung 58"', 4000)
car.add_produto(monitor)
car.add_produto(cerveja)
car.add_produto(cerveja)
car.finalizar_compra()
