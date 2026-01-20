from src.services.CaracteristicasPlantas import CaracteristicasPlanta
from src.services.ClassificadorPlantas import ClassificadorPlantas
from src.angiosperma import Angiosperma
from src.briofita import Briofita
from src.gimnosperma import Gimnosperma
from src.pteridofita import Pteridofita

from src.services.CatalogoService import CatalogoService

classificador = ClassificadorPlantas()
catalogo_service = CatalogoService()
catalogos = catalogo_service.carregar()

def formatar_planta(planta):
    texto = (        
        "\n--- Ficha Técnica ---\n"
        f"Nome Popular: {planta['Nome Popular']}\n"
        f"Nome Científico: {planta['Nome Científico']}\n"
        f"Região: {planta['Região']}\n"
        f"Classificação: {planta['Classificação']}\n"
        "---------------------\n")
    return texto

def converter_bool(resposta):
    if resposta == 'sim':
        return True
    else:
        return False

print('------   MENU    ------')
print('1 - Classificar uma nova planta')
print('2 - Listar planta no catálogo')
print('3 - Sair')

while True:
    opc = int(input('Insira o número da opção que você escolher: '))
    if opc == 1:
        nome_popular = input('Nome popular: ').lower()
        nome_cientifico = input('Nome científico: ').lower()
        regiao = input('Qual a região: ')
        print('Características da planta:')
        reproduz_por_esporos = converter_bool(input('Reproduz por esporos: (Sim ou Não) ').lower())
        possui_vasos = converter_bool(input('Possui vasos: (Sim ou Não) ').lower())
        possui_sementes = converter_bool(input('Possui Sementes: (Sim ou Não) ').lower())
        possui_flores = converter_bool(input('Possui Flores: (Sim ou Não) ').lower())
        possui_frutos = converter_bool(input('Possui Frutos: (Sim ou Não) ').lower())    
        carac_planta = CaracteristicasPlanta(possui_flores, possui_frutos, possui_vasos, reproduz_por_esporos, possui_sementes, regiao)
        classificacao = classificador.sugerir_classificacao(carac_planta)

        if classificacao == 'Angiosperma':
            planta_user = Angiosperma(nome_cientifico, nome_popular, regiao)
            planta_user.exibir_informacoes()
            catalogos.append(planta_user.formatar())
            catalogo_service.salvar(catalogos)
        elif classificacao == 'Briofita':
            planta_user = Briofita(nome_cientifico, nome_popular, regiao)
            planta_user.exibir_informacoes()
            catalogos.append(planta_user.formatar())
            catalogo_service.salvar(catalogos)
        elif classificacao == 'Gimnosperma':
            planta_user = Gimnosperma(nome_cientifico, nome_popular, regiao)
            planta_user.exibir_informacoes()
            catalogos.append(planta_user.formatar())
            catalogo_service.salvar(catalogos)
        elif classificacao == 'Pteridófita':
            planta_user = Pteridofita(nome_cientifico, nome_popular, regiao)
            planta_user.exibir_informacoes()
            catalogos.append(planta_user.formatar())
            catalogo_service.salvar(catalogos)
        else:
            print('Indefinido')
    elif opc == 2:
        print('\n--- CONSULTAR CATÁLOGO ---')
        print('1 - Por região')
        print('2 - Por classificação')
        print('3 - Listar tudo')

        escolha = int(input('Escolha uma opção: '))
        if escolha == 1:
            regiao_busca = input('Informe a região: ').lower()
            for planta in catalogos:
                if planta['Região'].lower() == regiao_busca:
                    print(formatar_planta(planta))
        elif escolha == 2:
            print('Angiosperma | Briofita | Gimnosperma | Pteridófita')
            classe = input('Informe a classificação: ')
            for planta in catalogos:
                if planta['Classificação'].lower() == classe:
                    print(formatar_planta(planta))
        elif escolha == 3:
            for planta in catalogos:
                print(formatar_planta(planta))
    elif opc == 3:
        break