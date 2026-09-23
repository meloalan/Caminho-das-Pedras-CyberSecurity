# Fundamentos de KQL

[← Índice do módulo](README.md) · [Página principal](../README.md)

## Conceito

KQL é uma linguagem de consulta orientada a tabelas. O pipeline passa o resultado de um operador ao seguinte. Nomes de colunas, tipos e período são parte do contrato da consulta.

## Prática orientada

Comece pelo exercício sintético abaixo; depois use o [catálogo](../queries/kql/README.md) em uma fonte real com esquema conferido.

## Entrega para o portfólio

Query comentada com pergunta, resultado esperado e resultado obtido.

## Critério de conclusão

Explique o resultado com suas palavras, registre as limitações e diferencie o que foi observado do que foi inferido. Dados de laboratório devem ser anonimizados antes da publicação.

## Exercício sintético sem ingestão

Os nomes e IP abaixo são fictícios; o bloco é apenas um conjunto de teste. Execute em um editor KQL compatível.

```kql
datatable(Host:string, EventID:int, SourceIP:string)
[
    "LAB-01", 4625, "192.0.2.10",
    "LAB-01", 4625, "192.0.2.10",
    "LAB-01", 4624, "192.0.2.10",
    "LAB-02", 4625, "192.0.2.20"
]
| where EventID == 4625
| summarize Failures = count() by Host
| sort by Failures desc
```

Procura falhas por host: `datatable` cria quatro linhas, `where` mantém três, `summarize` conta por host e `sort` ordena. Esperado: LAB-01 = 2 e LAB-02 = 1. Não há diagnóstico de ameaça: erros de senha também contariam. Melhoria: incluir horário, conta e contexto. Resultado de execução: pendente.
