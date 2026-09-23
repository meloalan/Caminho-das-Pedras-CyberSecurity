# Saúde da coleta

[← Catálogo KQL](README.md) · [Página principal](../../README.md)

## O que procura

Resume volume e último evento por computador observado.

## Query

[Arquivo executável em KQL](05-saude-coleta.kql)

```kql
// Verifica apenas hosts presentes: não detecta sozinho hosts totalmente ausentes.
SecurityEvent
| where TimeGenerated >= ago(24h)
| summarize Events = count(), LastSeen = max(TimeGenerated) by Computer
| extend Silence = now() - LastSeen
| sort by LastSeen asc
```

## Como funciona

O filtro limita a busca; `summarize` agrupa por Computer; `extend` calcula tempo desde o último evento; `sort` destaca dados antigos.

## Possíveis false positives

Host desligado, pouco uso ou coleta intencionalmente limitada podem explicar silêncio.

## Como melhorar

Cruzar com inventário esperado e sinais do agente. Separar atraso, falta de geração e falha de transporte. Não interpretar ausência de resultado como ambiente saudável.

## Validação

Exemplo educacional, ainda não executado em um workspace real. Confira esquema, provedor, auditoria e intervalo de tempo antes de usar. Resultado vazio também pode indicar falha de coleta.

TODO: adicionar evidência real do laboratório
