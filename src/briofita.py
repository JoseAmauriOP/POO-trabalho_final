from .planta import Planta

class Briofita(Planta):

    def exibir_informacoes(self):
        print(f"\n--- Ficha Técnica: ---")
        print(f"Nome Popular: {self.nome_popular}")
        print(f"Nome Científico: {self.nome_cientifico}")
        print(f"Região: {self.regiao}")
        print(f"Grupo: Briofita")
        print(f"Caracteristicas Gerais:")
        print(f"- Ausênsia de Flores")
        print(f"- Ausência de Frutos")
        print(f"- Ausência de Sementes")
        print(f"- Possui Esporos")
        print("-" * 40)    

    def formatar(self):
        return {
            'Nome Popular': self.nome_popular,
            'Nome Científico':self.nome_cientifico,
            'Região':self.regiao,
            'Classificação': 'Briofita'
            }    