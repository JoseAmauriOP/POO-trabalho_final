class Planta:
    def __init__(self, nome_cientifico, nome_popular, regiao):
        self.nome_cientifico = nome_cientifico
        self.nome_popular = nome_popular
        self.regiao = regiao

    def exibir_informacoes(self):
        print(f"\n--- 🌿 Ficha Técnica: {self.nome_popular} ---")
        print(f"Nome Científico: {self.nome_cientifico}")
        print(f"Região: {self.regiao}")
        print("-" * 40)