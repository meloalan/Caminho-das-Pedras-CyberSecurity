# Lab 07: Gaps de cobertura

[← Laboratórios](README.md) · [Avaliação de cobertura](../detection-coverage.md)

## Objetivo

Distinguir falta de fonte, falta de lógica, falta de validação e falta de resposta.

## Cenários

- A: um terço dos endpoints não envia o log exigido pela regra.
- B: todos os ativos em escopo enviam os dados, mas não há regra ou busca relevante.
- C: há regra e logs, mas nenhum teste ou owner conhece seus limites.
- D: há alerta validado, mas ninguém definiu triagem ou escalonamento.

## Tarefas

1. Classifique cada gap.
2. Registre a evidência que sustenta a classe.
3. Defina uma ação, responsável e critério de conclusão.
4. Explique por que não somaria as quatro situações num percentual único de matriz.

## Entrega

Use [Coverage Assessment](../TEMPLATE-COVERAGE-ASSESSMENT.md). Priorize pelo risco e pelo impacto no ambiente, não pela quantidade de células.
