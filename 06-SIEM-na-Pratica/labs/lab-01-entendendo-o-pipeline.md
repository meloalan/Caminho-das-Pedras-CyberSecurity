# Lab 01: Entendendo o pipeline

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-primeiras-consultas.md)

> Pergunta: em qual etapa um registro pode desaparecer?

## Objetivo e pré-requisitos

Acompanhar uma observação da origem à busca e distinguir geração, coleta, parsing e indexação. Leia [pipeline](../log-pipeline.md). Offline, use o primeiro 4625 do dataset. Com ambiente, use uma atividade benigna já autorizada e observada em VM própria.

## Execução

1. Anote provider, canal, ID, host, timestamp e identificador do registro.
2. Identifique o componente que lê a fonte e seu escopo de canais/filtros.
3. Descreva transporte, fila e destino. Se não puder observá-los, marque como desconhecidos.
4. Compare o original com campos pesquisáveis, separando ator e alvo.
5. Verifique se o tempo de busca corresponde à ocorrência ou processamento.
6. Simule no papel um canal ausente e use a árvore de troubleshooting para localizar a primeira evidência faltante.

## Caminhos por plataforma

| Ambiente | Onde acompanhar |
| --- | --- |
| Wazuh | Agent → manager → alerts/archives → indexer |
| Splunk | Input/forwarder → index → source/sourcetype/campos |
| QRadar | Log source → Collector/DSM → Processor/Ariel |
| Sentinel | Fonte → AMA/DCR no caminho escolhido → tabela |

## Resultado esperado e falhas úteis

O contrato identifica origem e destino sem confundir conectividade com completude. Offline, o campo timestamp é ocorrência definida pelo exercício; em Wazuh real, compare timestamp e systemTime. Um evento presente na origem e ausente no índice exige investigar coleta/processamento, não criar regra nova.

## Entrega

Tabela etapa × evidência × responsável × lacuna, com um diagnóstico e seu próximo teste. Critério de conclusão: conseguir explicar onde a prova de chegada termina.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](README.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-02-primeiras-consultas.md)
