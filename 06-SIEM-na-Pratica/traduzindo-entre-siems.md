# Traduzindo entre SIEMs: a pedra de Roseta

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](query-languages.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](windows-events.md)

## Traduza a intenção, depois a sintaxe

Use os [contratos e a primeira investigação explicada](query-languages.md) antes desta referência. Não são consultas universais copiáveis em qualquer implantação. Campos Lab do QRadar e aliases lab do Splunk são criados no exercício. Query DSL pressupõe mappings adequados no indexer Wazuh e archives pesquisáveis. Todas as identidades, hosts e endereços abaixo são fictícios.

Os blocos de cada intenção são alternativas para o mesmo problema. AQL aparece em fence `sql` por compatibilidade de realce. Query DSL usa corpos JSON para o endpoint indicado. Resultado vazio exige investigar cobertura e schema, não concluir benignidade.

## 1. Encontrar falhas de autenticação

Pergunta: quais registros descrevem falhas, no conjunto e janela selecionados? Valide conta alvo, autoridade, host, origem, LogonType e códigos da falha. Veja explicação linha por linha em linguagens.

### Wazuh: API do indexer: encontrar falhas de autenticação

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
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

### Splunk: SPL: encontrar falhas de autenticação

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625
| table _time EventCode lab_user lab_host lab_source_ip lab_logon_type
```

### QRadar: AQL: encontrar falhas de autenticação

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: encontrar falhas de autenticação

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625
| project TimeGenerated, Computer, TargetUserName, TargetDomainName, IpAddress, LogonType, Status, SubStatus
```

## 2. Encontrar criação de usuário

Quem criou a conta e quem foi criado? O ID não informa sozinho grupos ou logons posteriores.

### Wazuh: API do indexer: encontrar criação de usuário

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4720"
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

### Splunk: SPL: encontrar criação de usuário

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4720
| table _time EventCode lab_actor lab_user lab_host lab_domain
```

### QRadar: AQL: encontrar criação de usuário

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabActor", "LabUser", "LabDomain", "LabComputer"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4720'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: encontrar criação de usuário

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4720
| project TimeGenerated, Computer, SubjectUserName, SubjectDomainName, TargetUserName, TargetDomainName, TargetSid
```

## 3. Encontrar execução de processos

Quais processos foram criados? Aqui usamos Security 4688. Sysmon 1 requer outro provedor e canal, explicado abaixo.

### Wazuh: API do indexer: encontrar execução de processos

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4688"
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

### Splunk: SPL: encontrar execução de processos

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4688
| table _time EventCode lab_host _raw
```

### QRadar: AQL: encontrar execução de processos

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4688'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: encontrar execução de processos

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4688
| project TimeGenerated, Computer, SubjectUserName, NewProcessName, NewProcessId, CommandLine
```

## 4. Filtrar por usuário

Em quais eventos de falha aparece esta conta alvo? Preserve domínio para não misturar contas homônimas.

### Wazuh: API do indexer: filtrar por usuário

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
          }
        },
        {
          "term": {
            "data.win.eventdata.targetUserName": "lab-user"
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

### Splunk: SPL: filtrar por usuário

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625 lab_user="lab-user"
```

### QRadar: AQL: filtrar por usuário

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625' AND "LabUser" = 'lab-user'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: filtrar por usuário

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625 and TargetUserName == "lab-user"
```

## 5. Filtrar por hostname

O host é o emissor original, não o coletor WEF. Compare nomes curtos e FQDN antes de filtrar.

### Wazuh: API do indexer: filtrar por hostname

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
          }
        },
        {
          "term": {
            "data.win.system.computer": "WIN-LAB01"
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

### Splunk: SPL: filtrar por hostname

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625 lab_host="WIN-LAB01"
```

### QRadar: AQL: filtrar por hostname

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625' AND "LabComputer" = 'WIN-LAB01'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: filtrar por hostname

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625 and Computer == "WIN-LAB01"
```

## 6. Filtrar por IP

Quais falhas registraram este endereço? NAT e IP ausente limitam a associação com uma pessoa.

### Wazuh: API do indexer: filtrar por ip

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
          }
        },
        {
          "term": {
            "data.win.eventdata.ipAddress": "192.0.2.25"
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

### Splunk: SPL: filtrar por ip

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625 lab_source_ip="192.0.2.25"
```

### QRadar: AQL: filtrar por ip

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625' AND "LabSourceIP" = '192.0.2.25'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: filtrar por ip

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625 and IpAddress == "192.0.2.25"
```

## 7. Contar eventos

Pergunta: qual volume existe antes de limitar linhas para exibição? No Wazuh leia `hits.total.value`, não o tamanho de hits retornados. Em AQL mostramos registros e eventos representados separadamente.

### Wazuh: API do indexer: contar eventos

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
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

### Splunk: SPL: contar eventos

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625
| stats count AS total
```

### QRadar: AQL: contar eventos

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT COUNT(*) AS registros, SUM(eventcount) AS total
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625'

LAST 24 HOURS
```

### Sentinel: KQL: contar eventos

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625
| summarize Total=count()
```

## 8. Agrupar por usuário

Pergunta: como o volume se distribui? Campos ausentes precisam de acompanhamento separado. Os 20 buckets do Wazuh são um recorte, não uma lista completa.

### Wazuh: API do indexer: agrupar por usuário

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
          }
        }
      ]
    }
  },
  "aggs": {
    "distribuicao": {
      "terms": {
        "field": "data.win.eventdata.targetUserName",
        "size": 20
      }
    }
  }
}
```

### Splunk: SPL: agrupar por usuário

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625
| stats count AS total by lab_user
| sort 0 - total
```

### QRadar: AQL: agrupar por usuário

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT "LabUser", SUM(eventcount) AS total
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625'
GROUP BY "LabUser"
ORDER BY total DESC
LIMIT 20
LAST 24 HOURS
```

### Sentinel: KQL: agrupar por usuário

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625
| summarize Total=count() by TargetUserName
| order by Total desc
```

## 9. Agrupar por origem

Pergunta: como o volume se distribui? Campos ausentes precisam de acompanhamento separado. Os 20 buckets do Wazuh são um recorte, não uma lista completa.

### Wazuh: API do indexer: agrupar por origem

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
          }
        }
      ]
    }
  },
  "aggs": {
    "distribuicao": {
      "terms": {
        "field": "data.win.eventdata.ipAddress",
        "size": 20
      }
    }
  }
}
```

### Splunk: SPL: agrupar por origem

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625
| stats count AS total by lab_source_ip
| sort 0 - total
```

### QRadar: AQL: agrupar por origem

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT "LabSourceIP", SUM(eventcount) AS total
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625'
GROUP BY "LabSourceIP"
ORDER BY total DESC
LIMIT 20
LAST 24 HOURS
```

### Sentinel: KQL: agrupar por origem

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625
| summarize Total=count() by IpAddress
| order by Total desc
```

## 10. Ordenar por quantidade

Nas agregações acima, SPL usa `sort 0 - total`, AQL usa `ORDER BY total DESC` e KQL usa `order by Total desc`. O `terms` Wazuh ordena por contagem decrescente por padrão; para tornar explícito, inclua `"order": {"_count": "desc"}` dentro de `terms`. Ordenação não muda o significado da contagem. Inspecione empates, valores ausentes e truncamento antes de chamar o primeiro resultado de “mais perigoso”.

## 11. Criar uma janela absoluta

Pergunta: como reproduzir a análise do dia fictício 2026-09-20? Em Wazuh, substitua o range por `gte: "2026-09-20T00:00:00Z"` e `lt: "2026-09-21T00:00:00Z"`. Em SPL, use `earliest=1789862400 latest=1789948800`, limites Unix correspondentes ao mesmo intervalo UTC. Em AQL, substitua `LAST 24 HOURS` por `START '2026-09-20 00:00:00' STOP '2026-09-21 00:00:00'` **após configurar/verificar o fuso da pesquisa como UTC**. Em KQL, substitua o primeiro where por:

```kusto
| where TimeGenerated >= datetime(2026-09-20T00:00:00Z)
    and TimeGenerated < datetime(2026-09-21T00:00:00Z)
```

O trecho KQL é um operador para inserir após `SecurityEvent`, não uma consulta isolada. Confira as convenções de borda do produto ao comparar intervalos adjacentes. O `timestamp` Wazuh pode refletir processamento no manager; compare com `data.win.system.systemTime`. Para cronologia exata, normalize o tempo original, amplie a busca para atrasos e aplique o mesmo intervalo de ocorrência no conjunto validado.

## 12. Pesquisar várias condições

Pergunta: há falhas ou sucessos para a mesma conta? A busca conjunta produz candidatos; ainda não comprova uma sequência.

### Wazuh: API do indexer: pesquisar várias condições

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
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
              "4624",
              "4625"
            ]
          }
        },
        {
          "term": {
            "data.win.eventdata.targetUserName": "lab-user"
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

### Splunk: SPL: pesquisar várias condições

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now (EventCode=4624 OR EventCode=4625) lab_user="lab-user"
```

### QRadar: AQL: pesquisar várias condições

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND ("LabEventID" = '4624' OR "LabEventID" = '4625') AND "LabUser" = 'lab-user'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: pesquisar várias condições

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID in (4624, 4625) and TargetUserName == "lab-user"
| order by TimeGenerated asc
```

## 13. Excluir comportamento esperado

Pergunta: como retirar uma combinação previamente validada sem ocultar toda a conta? Exemplo didático exclui apenas `svc-lab` em `WIN-LAB02`; não é uma recomendação de allowlist. Registre motivo, owner, validade e teste de abuso da mesma identidade.

### Wazuh: API do indexer: excluir comportamento esperado

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-24h",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
          }
        }
      ],
      "must_not": [
        {
          "bool": {
            "filter": [
              {
                "term": {
                  "data.win.eventdata.targetUserName": "svc-lab"
                }
              },
              {
                "term": {
                  "data.win.system.computer": "WIN-LAB02"
                }
              }
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

### Splunk: SPL: excluir comportamento esperado

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625 NOT (lab_user="svc-lab" AND lab_host="WIN-LAB02")
```

### QRadar: AQL: excluir comportamento esperado

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625' AND NOT ("LabUser" = 'svc-lab' AND "LabComputer" = 'WIN-LAB02')
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL: excluir comportamento esperado

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625
| where not(TargetUserName == "svc-lab" and Computer == "WIN-LAB02")
```

## 14. Procurar sucessos depois de falhas

Use a busca de múltiplas condições, ordene pelo tempo de ocorrência validado e compare conta **com domínio**, host, origem e LogonType. A [correlação](correlation-rules.md) mostra uma query KQL com condições temporais, uma abordagem SPL e implementação por mecanismo nas quatro plataformas. Não use apenas “primeira falha antes do último sucesso”: isso pode juntar sessões não relacionadas em um dia inteiro.

No Wazuh, a Query DSL retorna documentos e agregações, mas não substitui regras temporais do manager. Em QRadar, AQL fornece candidatos e CRE implementa a regra operacional. Em Splunk, SPL pode expressar sequência, mas agendamento e throttle pertencem à configuração do alerta. No Sentinel, KQL fornece resultados e Analytics Rules define como gerar alertas/incidents.

## 15. Agregar no tempo e criar baseline simples

Pergunta: qual volume horário de falhas aparece na última semana? O resultado é uma série para comparação, não um modelo pronto de normalidade. Separe turno, dia útil, função do ativo, cobertura e períodos sem coleta. Uma semana observada pode conter incidentes ou mudanças.

### Wazuh: API do indexer: agregar no tempo e criar baseline simples

Corpo JSON para `POST /wazuh-archives-*/_search` no indexer, após habilitar e indexar archives.

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
              "gte": "now-7d",
              "lt": "now"
            }
          }
        },
        {
          "term": {
            "data.win.system.providerName": "Microsoft-Windows-Security-Auditing"
          }
        },
        {
          "term": {
            "data.win.system.eventID": "4625"
          }
        }
      ]
    }
  },
  "aggs": {
    "por_hora": {
      "date_histogram": {
        "field": "timestamp",
        "fixed_interval": "1h",
        "min_doc_count": 0
      }
    }
  }
}
```

### Splunk: SPL: agregar no tempo e criar baseline simples

```spl
index=windows source="XmlWinEventLog:Security" earliest=-7d latest=now EventCode=4625
| bin _time span=1h
| stats count AS total by _time
| sort 0 _time
```

### QRadar: AQL: agregar no tempo e criar baseline simples

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT DATEFORMAT(starttime,'yyyy-MM-dd HH') AS hora, SUM(eventcount) AS total
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625'
GROUP BY hora
ORDER BY hora ASC
LAST 7 DAYS
```

### Sentinel: KQL: agregar no tempo e criar baseline simples

```kusto
SecurityEvent
| where TimeGenerated >= ago(7d) and TimeGenerated < now()
| where EventID == 4625
| summarize Total=count() by bin(TimeGenerated, 1h)
| order by TimeGenerated asc
```

Compare uma hora atual com horas equivalentes do histórico, não com toda a semana misturada. Registre denominador e saúde. Histograma sem bounds não necessariamente mostra horas vazias nas bordas; SPL, AQL e KQL acima só retornam grupos presentes. Ausência de bucket não é zero confirmado.

## 16. Encontrar eventos raros

Pergunta: quais usuários aparecem em poucos registros de falha no período? Baixa frequência não significa risco. No Splunk, acrescente `| where total <= 2` após stats. Em KQL, `| where Total <= 2` após summarize. Em AQL, inclua `HAVING SUM(eventcount) <= 2` após GROUP BY e antes de ORDER BY. O limiar 2 é apenas didático.

No Wazuh, **não** use `terms` ordenado por contagem ascendente como inventário exato de raridade em vários shards. Para um laboratório pequeno, leia todos os documentos da janela usando paginação adequada e conte o conjunto validado, ou use agregação composite paginada conforme a versão do indexer. Declare completude, erro e limites antes de classificar raridade. O [Lab 09](labs/lab-09-threat-hunting.md) faz isso sobre o dataset completo, com resultado verificável.

## Sysmon exige outra seleção

Para Sysmon 1, confirme `Microsoft-Windows-Sysmon/Operational` e provedor `Microsoft-Windows-Sysmon`. Wazuh troca o filtro provider e Event ID; Splunk usa source/campos efetivamente configurados para Sysmon; QRadar precisa extrair LabProvider/LabEventID desse payload; Sentinel usa o exemplo WindowsEvent em [Sysmon e WEF](sysmon-wef.md). Um Event ID 1 sem provedor não identifica unicamente criação de processo.

## Prática e revisão

Escolha três intenções: localizar, agregar e relacionar. Anote pergunta, fonte, campos, tempo, resultado esperado, limite e consulta equivalente nas quatro plataformas. Valide apenas onde há ambiente e marque o restante como revisão conceitual. Consultas deste material foram revisadas contra a documentação, mas exigem execução e confirmação do schema na implantação real.

## Checkpoint

**Por que traduzir nomes de operadores não basta?**

<details>
<summary>Ver resposta</summary>

Modelos de dados, tipos, cobertura e unidade de contagem diferem.

</details>

**Como avaliar um resultado raro?**

<details>
<summary>Ver resposta</summary>

Com histórico adequado, completude, papel do ativo e contexto. Raro não é sinônimo de malicioso.

</details>

[← Tópico anterior](query-languages.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](windows-events.md)
