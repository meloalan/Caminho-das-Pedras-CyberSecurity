# Lab 04: PowerShell

[← Laboratórios](README.md) · [Técnicas](../techniques.md) · [Telemetria](../attack-to-telemetry.md)

## Objetivo

Interpretar T1059.001 com contexto e entender os limites de uma regra estreita.

## Regra fictícia

Uma regra alerta somente quando uma imagem específica inicia um argumento de execução codificada presente num campo de processo coletado. Os campos podem estar ausentes em alguns hosts. Nenhum comando ou payload é necessário para este exercício.

## Tarefas

1. Declare que manifestação a regra tenta observar.
2. Liste fonte e campos necessários, inclusive seu estado de coleta.
3. Descreva pelo menos três casos plausíveis que não seriam observados.
4. Explique por que uma tag T1059.001 não significa cobertura completa.
5. Proponha testes positivos, negativos e de campos ausentes em laboratório autorizado.

## Entrega

Registre um mapping e um resumo de limites. Não execute payloads nem use a regra para alegar cobertura de todas as plataformas ou formas de execução.
