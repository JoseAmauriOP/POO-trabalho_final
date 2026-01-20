import json
import os

class CatalogoService:
    def __init__(self, arquivo_db='catalogo.json'):
        self.arquivo_db = arquivo_db

    def salvar(self, dados):
        try:
            with open(self.arquivo_db, 'w', encoding='utf-8') as f:
                json.dump(dados, f, ensure_ascii=False, indent=4)
        except Exception as e:
            print(f"Erro ao salvar catálogo: {e}")

    def carregar(self):
        if not os.path.exists(self.arquivo_db):
            return []
        
        try:
            with open(self.arquivo_db, 'r', encoding='utf-8') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Erro ao ler o arquivo de catálogo. Iniciando vazio.")
            return []
        except Exception as e:
            print(f"Erro inesperado ao carregar: {e}")
            return []
