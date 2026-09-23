# Falhas seguidas de sucesso

[← Catálogo KQL](README.md) · [Página principal](../../README.md)

## O que procura

Encontra sucessos 4624 precedidos por pelo menos cinco 4625 para a mesma combinação de conta, host, IP e tipo de logon.

## Query

[Arquivo executável em KQL](04-falhas-seguidas-sucesso.kql)

```kql
// Regra educacional: >=5 falhas nos 10 minutos estritamente anteriores a cada sucesso.
// Conta + IP + host + tipo de logon. Campos vazios são excluídos (lacuna conhecida).
let Window = 10m;
let Threshold = 5;
let Base = SecurityEvent
| where TimeGenerated >= ago(70m)
| where EventID in (4624, 4625)
| extend AccountKey = tolower(TargetAccount), HostKey = tolower(Computer),
         SourceIP = tostring(IpAddress), LogonKey = tostring(LogonType)
| where isnotempty(AccountKey) and AccountKey != "-"
| where isnotempty(SourceIP) and SourceIP != "-"
| where isnotempty(HostKey) and isnotempty(LogonKey);
let Failures = Base
| where EventID == 4625
| project FailureTime = TimeGenerated, AccountKey, HostKey, SourceIP, LogonKey;
let Successes = Base
| where EventID == 4624 and TimeGenerated >= ago(1h)
| project SuccessTime = TimeGenerated, AccountKey, HostKey, SourceIP, LogonKey;
Successes
| join kind=inner (Failures) on AccountKey, HostKey, SourceIP, LogonKey
| where FailureTime < SuccessTime and FailureTime >= SuccessTime - Window
| summarize FailureCount = count(), FirstFailure = min(FailureTime), LastFailure = max(FailureTime)
    by SuccessTime, AccountKey, HostKey, SourceIP, LogonKey
| where FailureCount >= Threshold
| project SuccessTime, AccountKey, HostKey, SourceIP, LogonKey, FailureCount, FirstFailure, LastFailure
| sort by SuccessTime desc
```

## Como funciona

`let` define janela, limiar e conjuntos; 70 minutos incluem o histórico necessário ao início da hora. `join kind=inner` mantém todas as combinações de sucesso/falha. O filtro temporal exige que a falha anteceda o sucesso em até 10 minutos; `summarize` conta por sucesso. Não usa bins fixos, evitando perda na fronteira de um intervalo.

## Possíveis false positives

Usuário esqueceu a senha e depois acertou; serviço foi corrigido; IP compartilhado por NAT. O resultado é indício para triagem, não prova de comprometimento.

## Como melhorar

Validar deduplicação na origem: cópias de eventos inflam contagens; sucessos com timestamp idêntico podem se agrupar. Programação recorrente pode alertar repetidamente. Ajustar lookback, atraso de ingestão, agrupamento e identidade estável do evento conforme o conector. IPs diferentes, formatos distintos de conta e password spraying ficam fora desta lógica.

## Validação

Use o [teste sintético pronto](../tests/README.md) para comparar dez cenários com a mesma lógica, sem ingestão.

Exemplo educacional, ainda não executado em um workspace real. Confira esquema, provedor, auditoria e intervalo de tempo antes de usar. Resultado vazio também pode indicar falha de coleta.

TODO: adicionar evidência real do laboratório
