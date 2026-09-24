# Linguagens de busca em SIEM

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](parsing-normalizacao.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](traduzindo-entre-siems.md)

## Pergunta antes de linguagem

Vamos responder: “Quais falhas de autenticação foram registradas na janela disponível?” Isso exige fonte, tipo de evento, tempo, identidade e resultado. SPL, AQL, KQL e Query DSL expressam a intenção por modelos diferentes. A interface de busca pode acrescentar um filtro temporal próprio; confira se ele restringe ainda mais sua consulta.

## Contrato dos exemplos

| Ambiente | Pré-requisito declarado | O que não assumir |
| --- | --- | --- |
| Wazuh 4.14 | Indexer API, archives habilitados/indexados, campos eventchannel e mapping validado | Alertas não equivalem a todo evento; WQL do servidor não consulta esses índices |
| Splunk | Index `windows`, entrada XML Security, extração EventCode e aliases `lab_*` | Index, source, sourcetype e campos variam por implantação |
| QRadar SIEM | Propriedades Lab criadas no DSM Editor, tipo texto e extração validada | LabEventID não vem instalado por padrão; QID não é Event ID |
| Sentinel | Windows Security Events via AMA em SecurityEvent e permissão de consulta | WEF usa WindowsEvent no conector correspondente |

O padrão `source="XmlWinEventLog:Security"` é um exemplo para a entrada XML escolhida. Confira uma amostra sem esse filtro se sua configuração usa outro source. Sourcetype classifica o formato e não precisa ter o mesmo valor de source. Os aliases `lab_user`, `lab_host`, `lab_source_ip`, `lab_domain`, `lab_logon_type` correspondem aos campos da [normalização](parsing-normalizacao.md).

No QRadar, crie `LabProvider`, `LabEventID`, `LabUser`, `LabComputer`, `LabSourceIP`, `LabDomain`, `LabLogonType` a partir dos elementos originais, no escopo da fonte Windows. Todos são texto neste lab. Confirme a extração em amostras de 4624/4625. Não filtre por um campo desconhecido e interprete o erro como ausência de evento.

Os exemplos usam últimas 24 horas para um laboratório ao vivo. O dataset fornecido tem datas fixas: para ele, use janela absoluta que cubra **2026-09-20 UTC**, conforme a [pedra de Roseta](traduzindo-entre-siems.md). Não espere encontrar eventos de setembro com `ago(24h)` meses depois.

## A mesma investigação, quatro pesquisas

### Wazuh: API do indexer

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

### Splunk: SPL

```spl
index=windows source="XmlWinEventLog:Security" earliest=-24h latest=now EventCode=4625
| table _time EventCode lab_user lab_host lab_source_ip lab_logon_type
```

### QRadar: AQL

AQL usa o fence `sql` apenas para realce no GitHub; não é SQL genérico. Requer as propriedades Lab descritas no contrato.

```sql
SELECT starttime, "LabEventID", "LabUser", "LabComputer", "LabSourceIP"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
AND "LabEventID" = '4625'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
```

### Sentinel: KQL

```kusto
SecurityEvent
| where TimeGenerated >= ago(24h) and TimeGenerated < now()
| where EventID == 4625
| project TimeGenerated, Computer, TargetUserName, TargetDomainName, IpAddress, LogonType, Status, SubStatus
```

| Trecho | O que faz e como verificar |
| --- | --- |
| Wazuh `size` | Limita documentos retornados, não a população contada em total hits |
| Wazuh `range` | Restringe `timestamp`; compare-o ao horário original em systemTime |
| Wazuh `term` | Compara valor exato no mapping adequado; tipo e capitalização importam |
| SPL `index` e `source` | Selecionam o conjunto de dados; valide antes do filtro EventCode |
| SPL `earliest`/`latest` | Definem janela relativa no tempo indexado como `_time` |
| SPL `table` | Apresenta colunas; não cria os aliases ausentes |
| AQL `SELECT` e `FROM events` | Escolhem propriedades de registros Ariel de eventos |
| AQL `WHERE` | Aplica condições antes de agregações |
| AQL `ORDER BY`/`LIMIT` | Ordena e limita linhas exibidas, sem provar completude do caso |
| AQL `LAST 24 HOURS` | Restringe tempo de busca; não é um filtro de Event ID |
| KQL `SecurityEvent` | Seleciona uma tabela com schema específico |
| KQL `where` | Filtra janela e ID; confira se o evento usa esses campos |
| KQL `project` | Escolhe colunas, sem alterar os dados armazenados |

**Validação:** encontre uma falha benigna conhecida e confira host, usuário, domínio, IP quando presente, LogonType, horário e status/substatus. Conte sem limite de exibição se a pergunta for volume. Compare original e transformação antes de afirmar que quatro resultados diferentes são um erro do produto.

## Fundamentos comparados

| Intenção | Query DSL | SPL | AQL | KQL |
| --- | --- | --- | --- | --- |
| E / OU / exclusão | `bool.filter`, `should`, `must_not` | `AND`, `OR`, `NOT` com parênteses | `AND`, `OR`, `NOT` | `and`, `or`, `not()` |
| Contagem | Total hits ou `_count` | `stats count` | `COUNT(*)` ou `SUM(eventcount)` | `count`, `summarize count()` |
| Agrupar | `terms`, `date_histogram` | `stats ... by`, `bin` | `GROUP BY` | `summarize ... by`, `bin()` |
| Ordenar | `sort`, ordem do bucket | `sort` | `ORDER BY` | `order by` |
| Ausência | `exists` e sua negação | `isnull`, `isnotnull` | `IS NULL`, `IS NOT NULL` | `isempty`, `isnull` conforme tipo |
| Enriquecer | Ingestão/lookup ou camada de aplicação conforme arquitetura | `lookup` e modelos configurados | Reference data e funções compatíveis | `lookup`, `join`, watchlists/ASIM quando disponíveis |

`COUNT(*)` conta registros Ariel; `SUM(eventcount)` considera o contador de eventos em registros agregados/coalescidos. Defina a unidade antes de comparar com documentos do indexer ou linhas no Sentinel. `terms` retorna buckets limitados; top 10 não é inventário completo. A contagem agregada também depende de duplicatas e cobertura.

## Valores vazios e interpretação

Em um logon local, IP pode não estar preenchido. Não agrupe todas as ausências como se fossem uma mesma origem. Excluir dados vazios pode melhorar precisão e reduzir cobertura ao mesmo tempo. Meça quantos registros foram descartados e documente a decisão.

No KQL, operadores de comparação têm diferenças de sensibilidade a maiúsculas. Em SPL, use parênteses para tornar a intenção booleana explícita. Na Query DSL, `term` não é busca de texto analisado. Em AQL, propriedades e funções disponíveis dependem do schema/produto, não de um tutorial de SQL.

## Prática

Execute a primeira busca apenas no ambiente que você tem. Registre conjunto, janela, três campos preenchidos, um ausente e a contagem. Traduza a intenção para outra plataforma sem declarar que executou nela. Se não há ambiente, use o dataset e escreva o resultado esperado.

## Referências

- [Wazuh indexer API](https://documentation.wazuh.com/current/user-manual/indexer-api/reference.html): endpoints e parâmetros da busca.
- [Splunk add-on Windows](https://splunk.github.io/splunk-add-on-for-microsoft-windows/): formato, extrações e compatibilidade.
- [IBM AQL](https://www.ibm.com/docs/en/qsip/7.5.0?topic=aql-ariel-query-language): linguagem de consulta do Ariel.
- [KQL](https://learn.microsoft.com/en-us/kusto/query/): operadores de filtro, agregação e combinação.

## Checkpoint

**Uma query válida comprova que o campo está correto?**

<details>
<summary>Ver resposta</summary>

Não. Validade sintática, disponibilidade do campo e significado correto são verificações distintas.

</details>

**Por que os números podem diferir entre plataformas?**

<details>
<summary>Ver resposta</summary>

Cobertura, transformações, duplicação, coalescência, janela e unidade de contagem podem ser diferentes.

</details>

[← Tópico anterior](parsing-normalizacao.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](traduzindo-entre-siems.md)
