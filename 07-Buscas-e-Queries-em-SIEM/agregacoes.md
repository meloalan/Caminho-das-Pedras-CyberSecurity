# Agregações: o que exatamente você está contando?

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](tempo-em-queries.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](lookups-e-enriquecimento.md)

## GROUP BY muda a unidade de análise

Três falhas de LAB/alan.lab e uma de OUTRO/alan.lab não são quatro falhas da mesma identidade. Agrupe pela autoridade e pela conta quando esse for o objeto da pergunta. Host e origem podem ser dimensões adicionais.

| Métrica | Pergunta | Limitação |
| --- | --- | --- |
| count | Quantos registros? | Duplicação de ingestão infla o valor |
| count distinct | Quantos valores únicos? | Aproximação e valores ausentes variam |
| min / max | Primeira/última ocorrência ou extremos | Dois extremos não descrevem toda a sequência |
| avg | Qual média numérica? | Picos e populações diferentes podem desaparecer |
| sum | Qual soma de valores? | Unidade e coalescência precisam ser conhecidas |
| percentual | Qual parte de qual total? | Denominador deve usar mesma janela/população |

## Quantas falhas por usuário?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4625)
| summarize Total=count() by TargetDomainName, TargetUserName
| order by Total desc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4625)
| stats count AS total by lab_domain lab_user
| sort 0 -total
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT "LabDomain", "LabUser", SUM(eventcount) AS total
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4625')
GROUP BY "LabDomain", "LabUser"
ORDER BY total DESC
START '2026-09-24 00:00:00' STOP '2026-09-25 00:00:00'
```

</details>

<details>
<summary>Ver consulta em Query DSL no indexer Wazuh</summary>

```json
{
  "size": 0,
  "track_total_hits": true,
  "query": {
    "bool": {
      "filter": [
        {
          "range": {
            "timestamp": {
              "gte": "2026-09-24T00:00:00Z",
              "lt": "2026-09-25T00:00:00Z"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "4625"
            ]
          }
        }
      ]
    }
  },
  "aggs": {
    "dominios": {
      "terms": {
        "field": "data.win.eventdata.targetDomainName",
        "size": 50
      },
      "aggs": {
        "grupos": {
          "terms": {
            "field": "data.win.eventdata.targetUserName",
            "size": 50,
            "show_term_doc_count_error": true
          }
        }
      }
    }
  }
}
```

</details>

Use o [contrato](campos-e-schemas.md). Dataset esperado: LAB/alan.lab = 3, OUTRO/alan.lab = 1 e LAB/svc.lab = 1. AQL soma eventcount; Query DSL conta documentos nos buckets. Campo ausente pode não gerar grupo; meça ausências separadamente. Terms retorna buckets limitados e pode ter erro distribuído: consulte doc_count_error_upper_bound e sum_other_doc_count; para inventário completo use paginação composite apropriada.

## Quantas origens diferentes tentaram cada conta?

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID == 4625 and isnotempty(IpAddress) and IpAddress != "-"
| summarize by TargetDomainName, TargetUserName, IpAddress
| summarize Origens=count() by TargetDomainName, TargetUserName
```

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 EventCode=4625
| where len(lab_source_ip)>0 AND lab_source_ip!="-"
| stats dc(lab_source_ip) AS origens by lab_domain lab_user
```

```sql
SELECT "LabDomain", "LabUser", UNIQUECOUNT("LabSourceIP") AS origens
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625' AND "LabSourceIP" IS NOT NULL AND "LabSourceIP" <> '-' AND "LabSourceIP" <> ''
GROUP BY "LabDomain", "LabUser"
ORDER BY origens DESC
START '2026-09-24 00:00:00' STOP '2026-09-25 00:00:00'
```

Em Query DSL, cardinality de `data.win.eventdata.ipAddress` dentro do bucket da identidade estima cardinalidade, não é contagem exata universal. No KQL, `dcount()` também é estimador; a dupla agregação acima conta combinações observadas de modo explícito, podendo custar mais. Para comparar resultados, declare algoritmo, cobertura e tratamento de vazio.

## Top N e raridade

Ordene a contagem e limite depois de agregar. Top 10 usuários com falhas significa dez grupos de maior volume nessa população, não dez usuários atacados. Outros grupos podem ser relevantes. Empates precisam de critério adicional para saída estável.

Raro também depende do conjunto: um processo novo em um servidor recém-criado é diferente de um executável nunca observado em uma estação antiga. Não use terms ordenado por count ascendente como inventário confiável dos mais raros em múltiplos shards. [Hunting](threat-hunting.md) compara relações pai/filho e histórico com contexto.

## Referências e prática

[Agregações AQL](https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-aql-data-aggregation-functions) e [terms OpenSearch](https://docs.opensearch.org/latest/aggregations/bucket/terms/) descrevem unidades e limites. No dataset, quatro das cinco falhas estão em WIN-LAB01: 80% dos registros de falha, não 80% dos ataques.

## Checkpoint

**Uma linha de agregado ainda é um evento original?**

<details>
<summary>Ver resposta</summary>

Não. Ela representa um grupo e métricas. Preserve possibilidade de voltar aos registros que sustentam o grupo.

</details>

[← Tópico anterior](tempo-em-queries.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](lookups-e-enriquecimento.md)
