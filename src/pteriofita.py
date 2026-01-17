from planta import Planta

class Pteridófitas(Planta):

    def exibir_informacoes(self):
        print(f"\n--- Ficha Técnica: ---")
        print(f"Nome Popular: {self.nome_popular}")
        print(f"Nome Científico: {self.nome_cientifico}")
        print(f"Região: {self.regiao}")
        print(f"Grupo: Pteridófitas")
        print(f"Caracteristicas Gerais:")
        print(f"- Ausênsia de Flores")
        print(f"- Ausência de Frutos")
        print(f"- Possui  Sementes")
        print(f"- Possui Vasos Condutores")
        print("-" * 40)