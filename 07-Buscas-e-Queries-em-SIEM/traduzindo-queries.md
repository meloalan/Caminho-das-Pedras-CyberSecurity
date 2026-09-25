# A mesma pergunta em diferentes SIEMs

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](correlacao-e-joins.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](kql.md)

## Traduza intenção, não caracteres

Os exemplos operacionais usam o [contrato de campos](campos-e-schemas.md). KQL usa SecurityEvent ou WindowsEvent; SPL exige aliases `lab_*`; AQL exige propriedades `Lab*` configuradas; JSON é corpo de `POST /wazuh-archives-*/_search` na API do **indexer**, com archives habilitados e indexados. Não é WQL. O intervalo fixo é 24/09/2026 UTC; AQL requer conferir o fuso da Console. O dataset local representa a mesma intenção, mas não é um export nativo nem pode ser inserido diretamente em SecurityEvent.

| Quero fazer | KQL | SPL | AQL | Query DSL no indexer |
| --- | --- | --- | --- | --- |
| Igualdade | == ou =~ para string sem caixa | search =; where = conforme tipo | = | term em campo exato |
| Diferente | != / !~ | !=; cuidado com inexistentes | <> / != conforme operador | must_not; existência é separada |
| E | and | AND | AND | bool.filter / must |
| OU | or | OR | OR | should com mínimo explícito |
| Negação | not() | NOT em search; NOT em expressão | NOT | must_not |
| Contar | count() | count | COUNT(*) ou SUM(eventcount) | hits.total / doc_count |
| Agrupar | summarize by | stats by | GROUP BY | aggregations |
| Ordenar | order by | sort | ORDER BY | sort ou ordem de buckets |
| Top N | top | sort + head | ORDER BY + LIMIT | hits.size ou terms.size |
| Tempo | datetime / ago / bin | earliest/latest / bin | LAST / START/STOP / DATEFORMAT | range / date_histogram |
| Distintos | distinct ou agregação; dcount estima | dedup / dc | GROUP BY / UNIQUECOUNT | composite / cardinality estima |
| Relacionar | join / lookup | lookup / join / stats | reference data e lógica compatível | ingestão/aplicação; sem join SQL universal |

Um operador parecido não garante mesma população, unidade, precisão ou tratamento de null. O primeiro passo é conferir campos. As consultas abaixo recuperam amostras de eventos; as páginas de agregação e correlação desenvolvem contagem e relações. No JSON, `timestamp` é o relógio do documento; confirme o horário original para sequência. AQL pode representar eventos coalescidos.

## Falhas de autenticação

Quem tentou autenticar, de onde, em qual host, tipo e horário?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4625)
| project TimeGenerated, Computer, EventID, SubjectUserName, TargetUserName, TargetDomainName, IpAddress, LogonType
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4625)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_user lab_domain lab_source_ip lab_logon_type
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabUser", "LabDomain", "LabSourceIP", "LabLogonType"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4625')
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
  "sort": [
    {
      "timestamp": "asc"
    }
  ]
}
```

</details>

**Interpretação e limite:** Cinco falhas: quatro em WIN-LAB01 e uma em WIN-LAB02. Preserve domínio e usuário. Erro de senha legítimo conta também.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Autenticação aceita

Qual autenticação foi aceita e em qual contexto?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4624)
| project TimeGenerated, Computer, EventID, SubjectUserName, TargetUserName, TargetDomainName, IpAddress, LogonType, TargetLogonId
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4624)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_user lab_domain lab_source_ip lab_logon_type lab_session
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabUser", "LabDomain", "LabSourceIP", "LabLogonType", "LabSession"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4624')
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
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "4624"
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

**Interpretação e limite:** E04 é um sucesso atual; H02 está fora do dia. Sucesso pode ter grande volume e não prova autorização de toda ação posterior.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Conta criada

Quem criou qual conta e em qual autoridade?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4720)
| project TimeGenerated, Computer, EventID, SubjectUserName, TargetUserName, TargetDomainName, IpAddress, LogonType
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4720)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_user lab_domain lab_source_ip lab_logon_type
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabUser", "LabDomain", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4720')
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
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "4720"
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

**Interpretação e limite:** E09: admin.lab criou novo.lab no DC-LAB01. O dataset declara conta de domínio. Não há SourceIP nesse evento; não invente origem herdada.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Mudança de grupo

Qual membro foi adicionado, a qual grupo e por qual ator?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4728, 4732)
| project TimeGenerated, Computer, EventID, SubjectUserName, TargetUserName, TargetDomainName, MemberName, MemberSid, TargetSid
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4728 OR EventCode=4732)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_user lab_domain lab_member lab_group_sid
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabUser", "LabDomain", "LabMember", "LabGroupSID"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4728', '4732')
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
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "4728",
              "4732"
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

**Interpretação e limite:** E14 é grupo global de segurança; E15 é grupo local. Global não significa automaticamente privilegiado. Examine SID, escopo e política antes de classificar.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Conta bloqueada

Qual conta e computador chamador foram informados?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4740)
| project TimeGenerated, Computer, EventID, SubjectUserName, TargetUserName, TargetDomainName, IpAddress, LogonType
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4740)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_user lab_domain lab_source_ip lab_logon_type
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabUser", "LabDomain", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4740')
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
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "4740"
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

**Interpretação e limite:** E16 registra svc.lab; caller_computer não é automaticamente um IP de origem. O bloqueio merece contexto de serviço e política.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Kerberos

Qual etapa de Kerberos, principal, serviço e código de resultado?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4768, 4769, 4771)
| project TimeGenerated, Computer, EventID, SubjectUserName, TargetUserName, TargetDomainName, IpAddress, LogonType
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4768 OR EventCode=4769 OR EventCode=4771)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_user lab_domain lab_source_ip lab_logon_type
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabUser", "LabDomain", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4768', '4769', '4771')
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
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "4768",
              "4769",
              "4771"
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

**Interpretação e limite:** E17/E18/E19 representam TGT, ticket de serviço e falha de pré-autenticação. O fixture omite códigos/serviço: essa lacuna impede diagnóstico da causa.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Processo Windows

Que processo foi criado e qual pai/comando estão registrados?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (4688)
| project TimeGenerated, Computer, EventID, SubjectUserName, NewProcessName, ParentProcessName, CommandLine, NewProcessId
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=4688)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_image lab_parent lab_command lab_process_id
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabImage", "LabParent", "LabCommand", "LabProcessID"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" IN ('4688')
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
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "4688"
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

**Interpretação e limite:** E13 corrobora E12 de outra fonte. Não some os dois como duas execuções sem conferir PID, host, horário e cobertura.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Processo Sysmon

Qual execução possui esse ProcessGuid e qual é sua linhagem?

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

**Interpretação e limite:** E06 e E12 têm o mesmo executável e pais diferentes. E06 mantém sessão aberta com -NoExit; presença de PowerShell não é malícia.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Conexão Sysmon

Qual processo se associou a uma comunicação e qual direção/contexto?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
WindowsEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where Provider == "Microsoft-Windows-Sysmon"
| where EventID in (3)
| project TimeGenerated, Computer, EventID, EventData
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" earliest=1790208000 latest=1790294400 (EventCode=3)
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
AND "LabEventID" IN ('3')
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
              "3"
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

**Interpretação e limite:** E08 representa TCP para 198.51.100.20. Sysmon 3 não cobre ICMP genérico nem substitui captura de pacotes.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## DNS Sysmon

Qual processo consultou qual nome?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
WindowsEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where Provider == "Microsoft-Windows-Sysmon"
| where EventID in (22)
| project TimeGenerated, Computer, EventID, EventData
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" earliest=1790208000 latest=1790294400 (EventCode=22)
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
AND "LabEventID" IN ('22')
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
              "22"
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

**Interpretação e limite:** E07 consulta updates.example.test. Consulta DNS não prova conexão, resolução bem-sucedida ou intenção.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Security Log limpo

Qual identidade limpou o log e qual autorização existia?

<details>
<summary>Ver consulta em KQL</summary>

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24) and TimeGenerated < datetime(2026-09-25)
| where EventID in (1102)
| project TimeGenerated, Computer, EventID, SubjectUserName, TargetUserName, TargetDomainName, IpAddress, LogonType
| order by TimeGenerated asc
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Security" earliest=1790208000 latest=1790294400 (EventCode=1102)
| sort 0 _time
| table _time EventCode lab_host lab_actor lab_user lab_domain lab_source_ip lab_logon_type
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabEventID", "LabComputer", "LabActor", "LabUser", "LabDomain", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Eventlog'
AND "LabEventID" IN ('1102')
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
            "data.win.system.providerName": "Microsoft-Windows-Eventlog"
          }
        },
        {
          "terms": {
            "data.win.system.eventID": [
              "1102"
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

**Interpretação e limite:** E20 usa provedor Microsoft-Windows-Eventlog no canal Security, diferente de Security-Auditing. Considere manutenção, lacuna de evidência e preservação.

**Confira:** compare a amostra com o payload original. Se faltar campo, a consulta precisa de extração/projeção adicional antes de responder à pergunta inteira.

## Próximas perguntas

Para obter quantidades, use [agregações](agregacoes.md). Para pesquisar usuário, host ou IP, acrescente igualdade no campo validado antes da projeção/agrupamento. Para conta, mantenha domínio; para processos, preserve provedor; para origem, não confunda destino. [Strings](strings-e-regex.md) inclui pesquisa de PowerShell e [pivôs](pivot.md) encadeia novas perguntas.

Registre query, versão, janela, campos, resultado esperado e obtido. A comparação documental está feita; a execução em produtos depende do seu ambiente.

## Checkpoint

**Por que 1102 precisa de atenção ao provedor?**

<details>
<summary>Ver resposta</summary>

O evento de limpeza do Security Log usa Microsoft-Windows-Eventlog. Filtrar somente Security-Auditing pode excluí-lo mesmo no canal correto.

</details>

[← Tópico anterior](correlacao-e-joins.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](kql.md)
