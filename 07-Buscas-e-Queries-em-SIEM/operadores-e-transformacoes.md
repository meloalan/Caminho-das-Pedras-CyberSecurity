# Operadores e transformações: preserve o significado

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](campos-e-schemas.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](strings-e-regex.md)

## Cada operador responde a uma intenção

Filtrar um milhão de eventos até restarem apenas 4625 muda a população. Selecionar cinco colunas muda a apresentação. Agrupar por conta muda a unidade da linha. Essas operações não são sinônimos.

| Intenção | KQL | SPL clássico | AQL | Query DSL no indexer |
| --- | --- | --- | --- | --- |
| Filtrar | where | search / where | WHERE | bool.filter e queries |
| Selecionar | project | fields / table | SELECT colunas | _source |
| Contar | count / summarize count() | stats count | COUNT(*) ou SUM(eventcount) | hits.total / doc_count |
| Agrupar | summarize by | stats by | GROUP BY | aggregations |
| Ordenar | sort / order by | sort | ORDER BY | sort ou ordem dos buckets |
| Top N | top | sort e head | ORDER BY e LIMIT | size dos hits ou terms.size |
| Combinações únicas | distinct | dedup / stats by | GROUP BY das propriedades | composite ou terms com limites |
| Criar valor | extend | eval | expressão com alias | script/runtime depende do produto/versão |
| String em minúsculas | tolower() | lower() em eval | LOWER() | normalizer na indexação; não altera _source |
| Enriquecer | lookup / join | lookup | funções de reference data | ingestão, aplicação ou mecanismo compatível |

Uma projeção prematura pode retirar a chave necessária mais adiante. `dedup` guarda representantes e depende da ordenação; não significa que eventos com mesmo usuário são duplicados. Para remover duplicação de coleta, defina ID de registro+host+canal+contexto, preservando cópia original para auditoria.

## Exemplo operacional: filtrar, selecionar e ordenar

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

Use o contrato de [campos](campos-e-schemas.md) e a janela fixa dos labs. KQL e SPL mantêm o detalhe do evento; AQL limita a 50 registros, que podem representar coalescência; JSON limita a 50 hits. Nenhum desses limites autoriza contar apenas a amostra como total.

## Booleanos e precedência

Considere A = 4625, B = 4624, C = host WIN-LAB01. `A OR B AND C` pode incluir falhas de qualquer host quando AND é avaliado primeiro. `(A OR B) AND C` restringe os dois tipos ao host escolhido.

| A | B | C | A OR (B AND C) | (A OR B) AND C |
| --- | --- | --- | --- | --- |
| verdadeiro | falso | falso | verdadeiro | falso |
| falso | verdadeiro | verdadeiro | verdadeiro | verdadeiro |
| falso | verdadeiro | falso | falso | falso |

Em SPL, `search` avalia OR antes de AND; `where` e `eval` avaliam AND antes de OR. Não transfira uma expressão sem parênteses entre esses contextos. Em KQL, use `and`, `or`, `not(...)`; em AQL, use agrupamentos explícitos. Query DSL usa objetos: `filter` combina requisitos; `must_not` exclui; um bloco `should` que deve ser obrigatório precisa de `minimum_should_match: 1` quando há filter/must.

Negar valor e exigir existência são decisões distintas. Um campo ausente pode ser mantido por must_not ou por certas expressões de search e eliminado por comparações que resultem em null. Teste ausente, vazio, hífen e valor válido. Não substitua ausência por “desconhecido” antes de medir o impacto da transformação.

## Transformação com contexto

```kusto
SecurityEvent
| where TimeGenerated >= ago(1h)
| extend HostNormalized=tolower(Computer)
| project Computer, HostNormalized, EventID
```

```spl
index=windows source="XmlWinEventLog:Security" earliest=-1h latest=now
| eval host_normalized=lower(lab_host)
| table lab_host host_normalized EventCode
```

Normalizar caixa não transforma nome curto em FQDN nem resolve renomeação. Preserve original e coluna derivada. Em AQL, `LOWER("LabComputer") AS host_normalized` é expressão de seleção; no indexer, prefira campo normalizado no contrato de ingestão quando necessário. Não prometa que scripts estejam habilitados ou sejam baratos.

## Subconsultas e relações

`let` KQL nomeia expressões e conjuntos; subsearch SPL tem limites de tempo e resultados; AQL tem recursos próprios, não todos os recursos de SQL; Query DSL não oferece um join SQL arbitrário entre índices. Consulte [correlação](correlacao-e-joins.md) e [enriquecimento](lookups-e-enriquecimento.md) antes de escolher o mecanismo.

## Referências e desafio

[Booleanos SPL](https://help.splunk.com/en/splunk-enterprise/search/search-manual/10.2/expressions-and-predicates/boolean-expressions-with-logical-operators) e [bool OpenSearch](https://docs.opensearch.org/latest/query-dsl/compound/bool/) fundamentam os cuidados acima.

Desafio: escreva a intenção “falha ou sucesso, apenas no host escolhido”, depois teste uma falha de outro host. A resposta correta exclui esse evento.

## Checkpoint

**Por que agrupar antes de filtrar pode mudar a resposta?**

<details>
<summary>Ver resposta</summary>

A agregação altera a granularidade e pode remover EventID ou outras chaves. Defina primeiro a população que a métrica deve representar.

</details>

[← Tópico anterior](campos-e-schemas.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](strings-e-regex.md)
