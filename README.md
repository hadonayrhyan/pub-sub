Atividade Processual: ***Sistemas Computacionais Distribuídos e Aplicações em Nuvens***
Professora: ***Ana Paula***
Alunos: ***Hadonay Rhyan e Kauã dos Santos***

***Objetivo***

O código tem como objetivo demonstrar o funcionamento do padrão Publish/Subscribe (Pub/Sub) aplicado a uma plataforma de Telemedicina e UTI. Equipamentos médicos enviam informações, enquanto sistemas como equipe médica, prontuário e painel de enfermagem recebem os dados de acordo com suas inscrições.

***Funcionamento***

O sistema possui três arquivos:

main.py: executa e organiza o sistema.

comunicacao.py: contém o Broker, responsável pelos tópicos e pelas operações de subscribe, unsubscribe e publish.

dispositivos.py: contém os equipamentos e sistemas hospitalares.

O fluxo funciona assim:

Equipamento → Broker → Subscriber

Um equipamento publica uma informação em um tópico, e o Broker encaminha essa informação para todos os sistemas inscritos naquele tópico.

***Execução***

Os três arquivos devem estar na mesma pasta. No terminal, dentro dessa pasta, execute:

python main.py

O programa mostrará as inscrições, mensagens publicadas, destinatários e o funcionamento do unsubscribe.
