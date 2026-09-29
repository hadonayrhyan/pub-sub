from comunicacao import CentralComunicacao

from dispositivos import (
    MonitorCardiaco,
    Oxigenio,
    PressaoArterial,
    EquipePlantao,
    Prontuario,
    PainelUTI
)


central = CentralComunicacao()


monitor = MonitorCardiaco(
    "Monitor cardíaco do leito 12",
    central
)

oximetro = Oxigenio(
    "Oxímetro do leito 12",
    central
)

pressao = PressaoArterial(
    "Medidor de pressão do leito 12",
    central
)


medicos = EquipePlantao(
    "Equipe médica"
)

prontuario = Prontuario(
    "Sistema de prontuário"
)

painel = PainelUTI(
    "Painel da enfermagem"
)


central.inscrever(
    "monitoramento",
    medicos.nome
)

central.inscrever(
    "monitoramento",
    prontuario.nome
)

central.inscrever(
    "monitoramento",
    painel.nome
)

central.inscrever(
    "alerta_cardiaco",
    medicos.nome
)

central.inscrever(
    "alerta_cardiaco",
    painel.nome
)

central.inscrever(
    "alerta_saturacao",
    medicos.nome
)

central.inscrever(
    "alerta_saturacao",
    painel.nome
)


oximetro.enviar(
    "monitoramento",
    "Saturação: 98% | FC: 76 bpm"
)

pressao.enviar(
    "monitoramento",
    "Pressão arterial: 118/79 mmHg"
)

monitor.enviar(
    "monitoramento",
    "Ritmo cardíaco dentro dos parâmetros."
)


monitor.enviar(
    "alerta_cardiaco",
    "Arritmia detectada no leito 12."
)

oximetro.enviar(
    "alerta_saturacao",
    "Saturação caiu para 87%."
)


print("\n===== CANCELAMENTO DE INSCRIÇÃO =====")

central.cancelar_inscricao(
    "monitoramento",
    painel.nome
)


oximetro.enviar(
    "monitoramento",
    "Nova leitura: Saturação 95% | FC 80 bpm"
)

