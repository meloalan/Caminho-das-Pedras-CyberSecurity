# Lab 06: Da query à regra

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-05-sysmon-process-creation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-tuning.md)

> Pergunta: como uma condição vira trabalho operacional?

## Objetivo e pré-requisitos

Especificar e testar a detecção simples de criação de usuário 4720. Leia [Detection Engineering](../detection-engineering.md), conclua o Lab 04 e confirme a fonte. Offline, produza a especificação e execute a matriz sobre amostras fictícias; não declare regra implantada.

## Execução

1. Declare objetivo, escopo local/domínio, dados necessários e owner fictício.
2. Escolha a implementação de sua plataforma na página de detecção.
3. Defina janela, frequência, entidades, severidade inicial e critérios de prioridade.
4. Teste 4720 válido, 4722, mesmo número em outro provider, ator/alvo distintos e campo ausente.
5. Teste duplicação e chegada tardia, mantendo cópia do original.
6. Escreva o alerta com referência de evidência e próximo passo.
7. Registre versão e procedimento de desativação/rollback da configuração de lab.

## Implementações

Wazuh usa XML de rule e logtest antes do manager. Splunk usa a busca salva e configuração de alerta. QRadar usa regra CRE, resposta e offense conforme configuração. Sentinel usa KQL mais Analytics Rule e entidades. Uma query da Roseta é parte da validação, não toda a implementação.

## Resultado esperado

O 4720 correto satisfaz a condição, preservando ator e alvo. Um 4722 não é criação. Outro provider não deve passar apenas porque o número coincide. Evento incompleto deve seguir política explícita e sinalizar lacuna.

## Entrega

Especificação, matriz esperado/obtido, alert sintético e limitações. Critério de conclusão: explicar quem recebe o resultado e como a regra será mantida, além de demonstrar que a consulta funciona.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-05-sysmon-process-creation.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-07-tuning.md)
