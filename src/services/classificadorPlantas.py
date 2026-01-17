from .caracteristicasPlantas import CaracteristicasPlanta

class ClassificadorPlantas():
    def sugerir_classificacao(self, planta_caract: CaracteristicasPlanta):
        if planta_caract.reproduz_por_esporos:
            if planta_caract.possui_vasos:
                return "Pteridófitas"
            else:
                return 'Briofita'
        elif planta_caract.possui_sementes:
            if planta_caract.possui_frutos and planta_caract.possui_flores:
                return 'Angiosperma'
            else:
                return 'Gimnosperna'
        else:
            return 'Indefinido.'
            