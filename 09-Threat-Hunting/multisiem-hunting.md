# Mesmo hunt, quatro plataformas

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](network-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunts.md)

## Hipótese e contrato comum

Pergunta: quais falhas antecederam um sucesso para a mesma identidade, host, origem e tipo de logon? A hipótese de uso indevido continua separada da observação dessa sequência. Exporte registros, verifique ordem e depois faça pivots de sessão. Não basta agregar “houve falha e sucesso no dia”.

Janela do exercício: [2026-09-24T08:00:00Z, 2026-09-24T10:00:00Z). Procure falhas nos dez minutos anteriores ao sucesso, mesmo domínio, usuário, host, IP e tipo. Dez minutos é um limite didático, não universal. Sem chave completa, registre associação inconclusiva; não agrupe todos os nulos.

O [contrato de campos do módulo 07](../07-Buscas-e-Queries-em-SIEM/campos-e-schemas.md) é pré-requisito. O JSON dos labs usa campos próprios e não foi ingerido nas plataformas. Os blocos abaixo são entradas de pesquisa, **não quatro motores equivalentes de correlação**.

## Sentinel: KQL

Contrato: tabela SecurityEvent, EventID inteiro, nomes do schema oficial. Computer deve corresponder a WIN-LAB01 no ambiente de teste; FQDN exige ajuste explícito. TimeGenerated deve ser conferido contra o horário original.

```kusto
SecurityEvent
| where TimeGenerated >= datetime(2026-09-24T08:00:00Z)
    and TimeGenerated < datetime(2026-09-24T10:00:00Z)
| where EventID in (4624, 4625)
| where Computer == "WIN-LAB01"
| project TimeGenerated, Computer, EventID, TargetDomainName,
    TargetUserName, IpAddress, LogonType, TargetLogonId,
    EventRecordId, EventSourceName, Channel, EventData
| order by TimeGenerated asc
```

Resultado esperado conceitual no fixture: E01/E02/E03/E04 e E10. Separe E10 pelo domínio; não o some às falhas de LAB/alan.lab. Confira limites de linhas/exportação no cliente. Para implementação de correlação, use [joins e tempo](../07-Buscas-e-Queries-em-SIEM/correlacao-e-joins.md), sem trocar automaticamente SecurityEvent por WindowsEvent ou Advanced Hunting.

## Splunk: SPL

Contrato: índice fictício windows e source XmlWinEventLog:Security; aliases LabHost, LabDomain, LabUser, LabSourceIP, LabLogonType, LabLogonId, LabEventRecordId, LabProvider e LabChannel previamente extraídos conforme módulo 07. EventCode vem do evento. Os epochs delimitam exatamente a janela UTC, independentemente do fuso da interface.

```spl
index=windows source="XmlWinEventLog:Security"
earliest=1790236800 latest=1790244000
(EventCode=4624 OR EventCode=4625) LabHost="WIN-LAB01"
| table _time EventCode LabHost LabDomain LabUser LabSourceIP LabLogonType LabLogonId LabEventRecordId LabProvider LabChannel _raw
| sort 0 _time
```

Não use o campo host do forwarder como sinônimo obrigatório do host original. sort 0 evita o limite padrão de sort, mas não elimina limites de exportação, permissões ou memória. O conjunto esperado tem a mesma ambiguidade de E10. Leia [SPL](../07-Buscas-e-Queries-em-SIEM/spl.md) para adaptar aliases e correlacionar sem perder os eventos originais.

## QRadar: AQL

Contrato: propriedades customizadas LabProvider, LabEventID (texto), LabHost, LabDomain, LabUser, LabSourceIP e LabLogonType extraídas/validadas no DSM. starttime deve representar o tempo selecionado; diferenças de horário de origem/armazenamento precisam de inspeção. Configure o contexto de pesquisa em UTC para as datas literais abaixo.

```sql
SELECT starttime, "LabEventID", "LabHost", "LabDomain", "LabUser",
       "LabSourceIP", "LabLogonType", eventcount
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Security-Auditing'
  AND "LabEventID" IN ('4624', '4625')
  AND "LabHost" = 'WIN-LAB01'
  AND starttime >= 1790236800000
  AND starttime < 1790244000000
ORDER BY starttime ASC
LIMIT 1000
START '2026-09-24 08:00:00' STOP '2026-09-24 10:00:00'
```

O WHERE em starttime aplica [08:00, 10:00) em epoch UTC com precisão de milissegundos; START/STOP restringe a busca Ariel, e o predicado explícito exclui a borda superior independentemente do arredondamento de STOP. AQL expõe starttime em milissegundos desde epoch; confira esse contrato na versão instalada. O limite 1000 exige checar truncamento. Coalescência pode representar várias ocorrências em eventcount e eliminar tempos individuais: não invente uma sequência a partir do peso. QID não é Windows Event ID. Pesquisa AQL não cria regra CRE nem offense. Consulte [AQL](../07-Buscas-e-Queries-em-SIEM/aql.md).

## Wazuh/OpenSearch: pesquisa no indexer

Use `POST /wazuh-archives-*/_search` em cliente autenticado de laboratório. Archives só está disponível se coleta, arquivamento, encaminhamento e indexação tiverem sido configurados. `wazuh-alerts-*` contém uma população filtrada por regras e pode omitir sucessos. WQL da API de agentes não é esta consulta.

Contrato: campos data.win.system.* exatos/keyword, eventID textual e systemTime mapeado como date. Verifique `_mapping` antes de executar; não acrescente `.keyword` sem existir. O campo computer é o host do evento, não necessariamente agent.name.

```json
{
  "size": 1000,
  "track_total_hits": true,
  "sort": [{"data.win.system.systemTime": "asc"}],
  "query": {
    "bool": {
      "filter": [
        {"term": {"data.win.system.providerName": "Microsoft-Windows-Security-Auditing"}},
        {"term": {"data.win.system.channel": "Security"}},
        {"terms": {"data.win.system.eventID": ["4624", "4625"]}},
        {"term": {"data.win.system.computer": "WIN-LAB01"}},
        {"range": {"data.win.system.systemTime": {
          "gte": "2026-09-24T08:00:00Z", "lt": "2026-09-24T10:00:00Z"
        }}}
      ]
    }
  }
}
```

Recupere `targetUserName`, `targetDomainName`, `ipAddress`, `logonType` e `targetLogonId` sob data.win.eventdata conforme presentes. Confira total versus hits retornados e paginação suportada; empates precisam de ordenação estável adicional ao paginar. Sem cobertura/mapping, zero hits não refuta a hipótese. Veja [camadas Wazuh/OpenSearch](../07-Buscas-e-Queries-em-SIEM/wazuh-opensearch.md).

## Identidade da evidência e duplicatas

Preserve identificador do registro original, host, canal/provedor e contexto de geração do log. EventRecordId pode reiniciar após limpeza/recriação do canal; não é chave global. No KQL, EventData é dado associado ao evento, não garantia de XML bruto completo: mantenha referência à coleta original quando necessária. No SPL, LabEventRecordId é alias explícito do EventRecordID de origem e `_raw` preserva o payload ingerido.

No QRadar, exporte também a propriedade customizada de EventRecordID e referência ao payload quando disponíveis; coalescência pode impedir reconstrução de ocorrências individuais. No indexer, preserve `_index`, `_id`, `_source` e o eventRecordID de origem; um novo documento pode ser reenvio do mesmo evento. Só remova duplicatas com identidade validada e conteúdo compatível. Não deduplique pelo conjunto de usuário, horário e resultado, pois tentativas reais distintas podem compartilhar esses campos. Sem identidade suficiente, registre a ambiguidade antes de contar.

## Interpretação e próximo pivot

As quatro consultas selecionam candidatos. Para cada sucesso, compare falhas anteriores com chave completa, janela e deduplicação; no fixture, E01/E02/E03 → E04. Depois consulte sessão 0xA100 no WIN-LAB01 e a execução E06. Registre query v1/v2, campos, tempo, resultados e limitações no journal.

Sem plataforma, faça o [Lab 10](labs/lab-10-multisiem-hunt.md) comparando os contratos e os registros. A revisão documental dos exemplos não equivale a execução em quatro produtos.

## Checkpoint

**Por que os mesmos filtros podem retornar populações diferentes?**

<details>
<summary>Ver resposta</summary>

Coleta, retenção, permissões, schema, coalescência, índices e limites de pesquisa diferem. Compare esses contratos antes de comparar contagens.

</details>

[← Tópico anterior](network-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](hunts.md)
