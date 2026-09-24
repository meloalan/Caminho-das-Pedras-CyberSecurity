# Lab 03: Autenticação Windows

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-02-primeiras-consultas.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-user-creation.md)

> Pergunta: as falhas e o sucesso pertencem ao mesmo contexto?

## Objetivo e pré-requisitos

Investigar 4625 e 4624 sem concluir ataque pela sequência. Leia [correlação](../correlation-rules.md). Com laboratório próprio, o [Lab 01 anterior](../../12-Labs-Praticos/01-EventID-4625/README.md) orienta uma falha manual benigna. Não gere ataques ou repetição automatizada.

## Execução

1. Selecione falhas e sucesso do dataset e ordene a ocorrência.
2. Compare target_user, target_domain, host, source_ip e logon_type.
3. Separe a conta homônima de OUTRO-LAB e a conta svc-lab.
4. Conte apenas falhas anteriores ao sucesso e dentro da janela didática de dez minutos.
5. Registre status/substatus quando disponíveis e não invente os ausentes.
6. Formule hipóteses de digitação, credencial antiga, tarefa/aplicação e uso não autorizado.
7. Escolha uma fonte/contexto adicional que possa discriminar as hipóteses.

## Quatro ambientes

Wazuh exige eventos de sucesso e falha pesquisáveis, não apenas alerts. Splunk usa chaves extraídas e pode examinar sequência com streamstats. QRadar separa candidatos AQL de estado CRE. Sentinel usa KQL com comparação temporal. Em todos, revise duplicação, precisão e campos ausentes.

## Resultado esperado

Uma sequência candidata reúne três falhas e um sucesso da chave LAB/lab-user em WIN-LAB01, origem 192.0.2.25, LogonType 10 (RemoteInteractive). O resultado sustenta uma sequência observada, não sua causa. A falha homônima não entra no conjunto.

## Entrega

Tabela fato × hipótese × próximo teste, chave de correlação e prioridade justificada. Critério de conclusão: explicar por que o sucesso não confirma brute force e por que falhas não herdam uma sessão de sucesso automaticamente.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-02-primeiras-consultas.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-04-user-creation.md)
