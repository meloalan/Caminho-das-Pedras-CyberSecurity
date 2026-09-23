# Criação de conta

[← Catálogo KQL](README.md) · [Página principal](../../README.md)

## O que procura

Localiza criação de usuário e distingue o ator da conta criada.

## Query

[Arquivo executável em KQL](02-conta-criada.kql)

```kql
// Confirmar se a conta criada é local ou de domínio antes do mapeamento MITRE.
SecurityEvent
| where TimeGenerated >= ago(24h)
| where EventID == 4720
| project TimeGenerated, Computer, SubjectAccount, TargetAccount, TargetSid
| sort by TimeGenerated desc
```

## Como funciona

O primeiro filtro define o período; o segundo seleciona 4720. SubjectAccount representa o ator e TargetAccount/TargetSid identificam o alvo.

## Possíveis false positives

Provisionamento aprovado, instalação de aplicativos e tarefas de administração.

## Como melhorar

Correlacionar com chamado de mudança e adição a grupos privilegiados. T1136.001 só se a conta for local; em domínio revisar T1136.002.

## Validação

Exemplo educacional, ainda não executado em um workspace real. Confira esquema, provedor, auditoria e intervalo de tempo antes de usar. Resultado vazio também pode indicar falha de coleta.

TODO: adicionar evidência real do laboratório
