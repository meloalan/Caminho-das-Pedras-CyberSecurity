# Lab 09: Threat Hunting

[← Laboratórios](README.md) · [ATT&CK em Hunting](../attack-for-threat-hunting.md)

## Objetivo

Construir hipótese testável e documentar limitações da telemetria.

## Hipótese

“Algumas execuções de PowerShell fora do padrão administrativo podem não ser triadas pela regra atual.” Esta frase não afirma que houve atividade maliciosa.

## Tarefas

1. Delimite ativos, identidades e janela de tempo do exercício.
2. Liste fontes e campos disponíveis, ausentes e inconsistentes.
3. Defina atividade normal, hipótese, alternativas e critério de interesse.
4. Escreva consulta exploratória abstrata ou use dados sintéticos.
5. Registre achado negativo ou positivo sem inferir intenção apenas pelo nome do processo.

## Entrega

Pergunta, escopo, dados, consulta, limites, resultado e próximos passos. Um hunt sem resultado com coleta incompleta deve gerar uma pergunta de telemetria, não declarar ausência de comportamento.
