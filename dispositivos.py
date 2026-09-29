class MonitorCardiaco:

    def __init__(self, nome, central):
        self.nome = nome
        self.central = central

    def enviar(self, canal, informacao):
        print(f"\n{self.nome} registrou uma informação.")

        self.central.enviar(
            canal,
            informacao
        )


class Oxigenio:

    def __init__(self, nome, central):
        self.nome = nome
        self.central = central

    def enviar(self, canal, informacao):
        print(f"\n{self.nome} realizou uma medição.")

        self.central.enviar(
            canal,
            informacao
        )


class PressaoArterial:

    def __init__(self, nome, central):
        self.nome = nome
        self.central = central

    def enviar(self, canal, informacao):
        print(f"\n{self.nome} realizou uma medição.")

        self.central.enviar(
            canal,
            informacao
        )


class EquipePlantao:

    def __init__(self, nome):
        self.nome = nome


class Prontuario:

    def __init__(self, nome):
        self.nome = nome


class PainelUTI:

    def __init__(self, nome):
        self.nome = nome
