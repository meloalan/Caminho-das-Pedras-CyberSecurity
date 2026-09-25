# Criação de processo: consultas por caso de uso

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Catálogo](../README.md) · [Página principal](../../README.md)

## Pergunta e contrato

Qual processo, pai, comando e contexto foram observados?

Os exemplos operacionais usam o [contrato de campos](../../07-Buscas-e-Queries-em-SIEM/campos-e-schemas.md). KQL usa SecurityEvent ou WindowsEvent; SPL exige aliases `lab_*`; AQL exige propriedades `Lab*` configuradas; JSON é corpo de `POST /wazuh-archives-*/_search` na API do **indexer**, com archives habilitados e indexados. Não é WQL. O intervalo fixo é 24/09/2026 UTC; AQL requer conferir o fuso da Console. O dataset local representa a mesma intenção, mas não é um export nativo nem pode ser inserido diretamente em SecurityEvent.

## Quatro implementações

<details>
<summary>Ver consulta em KQL</summary>

```kusto
WindowsEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where Provider == "Microsoft-Windows-Sysmon"
| where EventID in (1)
| project TimeGenerated, Computer, EventID, EventData
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" earliest=1790208000 latest=1790294400 (EventCode=1)
| sort 0 _time
| table _time EventCode lab_host lab_user lab_image lab_parent lab_command lab_process_guid lab_destination_ip lab_query_name
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabUser", "LabImage", "LabParent", "LabCommand", "LabProcessGuid", "LabDestinationIP", "LabQueryName"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Sysmon'
AND "LabEventID" IN ('1')
ORDER BY starttime ASC LIMIT 50
START '2026-09-24 00:00:00' STOP '2026-09-25 00:00:00'
```

</details>

<details>
<summary>Ver consulta em Query DSL no indexer Wazuh</summary>

```json
{
  "size": 50,
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
            "data.win.system.providerName": "Microsoft-Windows-Sysmon"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "1"
            ]
          }
        }
      ]
    }
  },
  "sort": [
    {
      "timestamp": "asc"
    }
  ]
}
```

</details>

## Como validar

Compare amostra original, campos, janela e resultado. O [dataset](../../07-Buscas-e-Queries-em-SIEM/labs/dados/README.md) oferece resultados conceituais; ele não foi ingerido nas quatro plataformas. Query não implanta regra. Para sequência, consulte [correlação](../../07-Buscas-e-Queries-em-SIEM/correlacao-e-joins.md).
