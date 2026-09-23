# Data connectors

[← Índice do módulo](README.md) · [Página principal](../README.md)

## Conceito

Conectores definem como os dados chegam. Windows Security Events via AMA e regras de coleta precisam estar associados ao host correto. Sysmon não aparece automaticamente em SecurityEvent.

## Prática orientada

Confirme pré-requisitos no [catálogo oficial](https://learn.microsoft.com/en-us/azure/sentinel/data-connectors-reference). Verifique agente, associação da DCR, canal e tabela de destino. Gere um evento benigno e compare origem/destino.

## Entrega para o portfólio

Diagrama host → coleta → workspace, com um evento verificado ponta a ponta.

## Critério de conclusão

Explique o resultado com suas palavras, registre as limitações e diferencie o que foi observado do que foi inferido. Dados de laboratório devem ser anonimizados antes da publicação.
