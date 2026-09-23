# Falhas de autenticação

[← Catálogo KQL](README.md) · [Página principal](../../README.md)

## O que procura

Localiza eventos 4625 para investigar tentativas que falharam.

## Query

[Arquivo executável em KQL](01-falhas-autenticacao.kql)

```kql
// SecurityEvent: Windows Security Events via AMA. Exemplo educacional.
SecurityEvent
| where TimeGenerated >= ago(24h)
| where EventID == 4625
| project TimeGenerated, Computer, TargetAccount, IpAddress, LogonType, Status, SubStatus
| sort by TimeGenerated desc
```

## Como funciona

`where` limita tempo e ID; `project` seleciona contexto; `sort` mostra os eventos mais recentes. TargetAccount é a conta alvo, não necessariamente quem iniciou outra ação administrativa.

## Possíveis false positives

Senha digitada incorretamente, senha expirada e serviços com credenciais antigas. Um 4625 isolado não confirma brute force.

## Como melhorar

Examinar Status/SubStatus, tipo de logon e baseline por host. IP pode estar vazio, ser loopback ou não representar a origem final.

## Validação

Exemplo educacional, ainda não executado em um workspace real. Confira esquema, provedor, auditoria e intervalo de tempo antes de usar. Resultado vazio também pode indicar falha de coleta.

TODO: adicionar evidência real do laboratório
