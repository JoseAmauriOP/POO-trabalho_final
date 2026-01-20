from .planta import Planta

class Angiosperma(Planta):
    def exibir_informacoes(self):
        print(f"\n--- Ficha Técnica: Planta  ---")
        print(f"Nome Popular: {self.nome_popular}")
        print(f"Nome Científico: {self.nome_cientifico}")
        print(f"Região: {self.regiao}")
        print(f"Grupo: Angiosperma")
        print(f"Caracteristicas Gerais:")
        print(f"- Possui Flores")
        print(f"- Possui Frutos")
        print(f"- Possui Sementes")
        print("-" * 40)

    def formatar(self):
        return {
            'Nome Popular': self.nome_popular,
            'Nome Científico':self.nome_cientifico,
            'Região':self.regiao,
            'Classificação': 'Angiosperma'
            }
