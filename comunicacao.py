class CentralComunicacao:

    def __init__(self):
        self.canais = {}

    def inscrever(self, canal, participante):
        participantes = self.canais.setdefault(canal, [])

        if participante not in participantes:
            participantes.append(participante)

        print(
            f"[INSCRIÇÃO] {participante} "
            f"acompanhará '{canal}'."
        )

    def cancelar_inscricao(self, canal, participante):
        participantes = self.canais.get(canal, [])

        if participante in participantes:
            participantes.remove(participante)

            print(
                f"[CANCELAMENTO] {participante} "
                f"não acompanhará mais '{canal}'."
            )

    def enviar(self, canal, conteudo):
        print(f"\n[CANAL: {canal}]")
        print(f"Informação: {conteudo}")

        participantes = self.canais.get(canal, [])

        if not participantes:
            print("Nenhum sistema está acompanhando este canal.")
            return

        for participante in participantes:
            print(f" -> {participante} recebeu a informação.")
