# Lab 06: Falhas de login seguidas por sucesso

[← Índice da trilha](../README.md) · [Página principal](../../README.md) · [Lab 02: Logs](../lab-02-logs/README.md) · [Lab 05: Detecção](../lab-05-detection/README.md) · [Teste KQL existente](../../queries/tests/README.md)

**Aviso:** não faça brute force. Use a fixture sintética ou no máximo uma sequência manual pequena em conta descartável numa VM isolada. Nunca faça login de teste contra sistemas de terceiros.

## Objetivo

Investigar uma sequência hipotética com várias falhas 4625 seguidas por sucesso 4624. Aprenda por que limiar, janela, entidade e baseline alteram resultado.

## Hipótese e lógica

```text
Para cada evento 4624:
  procure 4625 anteriores numa janela móvel de 10 minutos
  agrupe por conta, host, origem e LogonType, se estes campos forem confiáveis
  gere candidato quando houver 5 ou mais falhas
  compare contexto, volume normal e possíveis sistemas de NAT
```

Cinco falhas em dez minutos é apenas um parâmetro didático. Um threshold menor pode gerar ruído; maior pode não detectar padrões lentos. Um sucesso depois de falhas não prova que alguém acertou senha, pois os eventos podem refletir usuário que errou e depois autenticou corretamente.

## Microsoft Sentinel, KQL

Esta é a query com fixtures do projeto. Ela agrupa por conta, computador, IP e LogonType; descarta chaves vazias; exige falha estritamente anterior ao sucesso. Veja implementação e [casos sintéticos](../../queries/kql/04-falhas-seguidas-sucesso.kql).

```kql
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
let Failures = Base | where EventID == 4625
| project FailureTime=TimeGenerated, AccountKey, HostKey, SourceIP, LogonKey;
let Successes = Base | where EventID == 4624 and TimeGenerated >= ago(1h)
| project SuccessTime=TimeGenerated, AccountKey, HostKey, SourceIP, LogonKey;
Successes
| join kind=inner Failures on AccountKey, HostKey, SourceIP, LogonKey
| where FailureTime < SuccessTime and FailureTime >= SuccessTime - Window
| summarize FailureCount=count(), FirstFailure=min(FailureTime), LastFailure=max(FailureTime)
    by SuccessTime, AccountKey, HostKey, SourceIP, LogonKey
| where FailureCount >= Threshold
| project SuccessTime, AccountKey, HostKey, SourceIP, LogonKey, FailureCount, FirstFailure, LastFailure
| order by SuccessTime desc
```

## Splunk, Elastic e QRadar

Correlação temporal exata depende de schema e capacidade de cada regra. Comece com a mesma tabela de teste: `timestamp, event_id, account, host, source_ip, logon_type`. Para cada implementação, defina eventos anteriores, chave de agrupamento, janela deslizante e condição de encerramento no sucesso. Teste eventos fora de ordem, chaves vazias, IP ausente, quatro e cinco falhas, falhas depois do sucesso e limites de tempo.

- **Splunk SPL:** `transaction` pode ajudar na exploração de uma sequência com `maxspan=10m`, mas depende de eventos ordenados, de contiguidade e de `startswith/endswith`. Para regra operável, teste agregação temporal e deduplicação com volume realista. Veja [streamstats](https://help.splunk.com/en/splunk-enterprise/search/spl2-search-reference/streamstats-command/streamstats-command-overview-syntax-and-usage).
- **Elastic:** use EQL sequence ou regra de threshold conforme versão/licença, schema ECS e campos de entidade. Teste `host.id`, `user.name`, `source.ip`, `winlog.logon.type` e timestamp conforme a integração. [EQL correlation](https://www.elastic.co/docs/solutions/security/detect-and-alert/eql) explica sequenciamento e limites.
- **QRadar AQL:** AQL permite explorar e agrupar eventos; regra temporal e estado são implementados no QRadar Custom Rule Engine (CRE), não por uma query pontual simples. Configure a sequência de falhas e sucesso com filtros por evento realmente extraídos do DSM. Valide a documentação IBM de [AQL](https://www.ibm.com/docs/en/qradar-on-cloud?topic=structure-select-statement) e [regras CRE](https://www.ibm.com/docs/en/qradar-on-cloud?topic=rules-custom-rule-engine).
- **Wazuh:** use regras de frequência/tempo com `if_matched_sid` e campos de correlação conforme decoder Windows instalado. Correlacionar falhas e sucesso exige IDs de regra estáveis e campos comuns; prove essa chave em alertas de teste antes de ativar.

Esses apontamentos descrevem a lógica comparável. Não copie uma sintaxe sem checar tabela, campos, unidade de tempo e mecanismo de correlação da versão instalada.

## Baseline, falsos positivos e pontos cegos

Usuário esqueceu senha, serviço com segredo vencido, suporte técnico, IP de proxy/NAT compartilhado, scanner autorizado e relógios desajustados podem produzir padrões parecidos. Campos IP vazios excluídos pela query criam ponto cego para logons locais. Outras contas e password spraying ficam fora de uma chave centrada numa conta.

## Testes mínimos

Use o [teste sintético dos módulos de queries](../../queries/tests/README.md), que tem dez casos, e acrescente os seus. A saída deve distinguir quatro de cinco falhas, ordem antes/depois, origem diferente, mesma hora, janela limite, host diferente e eventos duplicados. Não faça brute force para validar uma regra.

## Entrega

Registre limiar e justificativa local, janela, chaves, casos não observados, falsos positivos, atraso de ingestão e como o SOC investigaria. O próximo [Lab 07](../lab-07-telemetria/README.md) amplia a telemetria para Windows, Linux, firewall e cloud opcional.
