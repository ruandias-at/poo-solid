class ControleRemoto:

    def __init__ (self, tv: str, comodo: str):
        self.tv = tv
        self.comodo = comodo

    def avancar_canal(self) -> None:
        print("Canal Avançado")

    def voltar_canal(self) -> None:
        print("Canal Voltado")
    
    def escolher_canal(self, canal: int) -> None:
        print(f"Canal alterado para {canal}")

tv_sala = ControleRemoto('Samsung', 'Sala')
print(tv_sala.tv)
print(tv_sala.comodo)
tv_sala.avancar_canal()
tv_sala.escolher_canal(4)

tv_quarto = ControleRemoto('LG', 'Quarto')
print(tv_quarto.tv)
print(tv_quarto.comodo)
tv_quarto.voltar_canal()
tv_quarto.escolher_canal(8)
