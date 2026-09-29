# Lab 05: Primeira detecção, criação de conta

[← Índice da trilha](../README.md) · [Página principal](../../README.md) · [Lab 04: SIEM](../lab-04-siem/README.md) · [Lab 06: Correlação](../lab-06-brute-force/README.md) · [ATT&CK](../../11-MITRE-ATTACK/README.md)

**Pré-requisitos:** Lab 02 para gerar e reconhecer 4720, e um destino de pesquisa local ou remoto. **Status: exemplos educacionais, não regra implantada.**

## Pergunta de detecção

Que contas foram criadas no ambiente de laboratório? A lógica inicial gera uma observação para cada evento 4720 e retorna autor, alvo, computador e horário. Ainda não afirma que a criação foi maliciosa.

## Modelo da regra

```text
Quando evento Security de criação de usuário chegar
  selecione horário, computador, autor e conta alvo
  mantenha o evento original para investigação
  encaminhe para triagem com severidade inicial baixa
```

Antes de habilitar, confirme auditoria, origem, timezone, campos extraídos e população coletada. Um volume alto de provisionamento legítimo precisa de owner, baseline e processo de mudança.

## Exemplos por SIEM

Os blocos assumem schemas de exemplo. Verifique fonte, tabela, decoder, nomes e tipos dos campos antes de usar. Não são traduções idênticas nem regras prontas para produção.

### Microsoft Sentinel, KQL

Assume tabela `SecurityEvent` e coluna `EventID` inteira, como no conector usado pelos labs existentes.

```kql
SecurityEvent
| where TimeGenerated >= ago(24h)
| where EventID == 4720
| project TimeGenerated, Computer, SubjectAccount, TargetAccount, TargetSid
| order by TimeGenerated desc
```

Busca 4720 nas últimas 24 horas e retorna autor e alvo. `SubjectAccount` e `TargetAccount` variam entre conectores. Compare o XML. Veja a [query KQL do projeto](../../queries/kql/02-conta-criada.kql).

### Splunk, SPL

Assume `index=wineventlog`, sourcetype extraindo `EventCode`, `SubjectUserName` e `TargetUserName`. Ajuste para seu add-on e parser.

```spl
index=wineventlog EventCode=4720 earliest=-24h
| table _time host SubjectUserName TargetUserName TargetSid
| sort - _time
```

Filtra o mesmo tipo de evento e mostra entidades para revisão. Se seu source usa `EventID`, `user`, `dest` ou `src_user`, altere depois de inspecionar um evento bruto.

### IBM QRadar, AQL

Assume o DSM expõe a propriedade customizada `EventID` como propriedade normalizada. No QRadar, valide os campos do evento no Log Activity. Se não houver propriedade ID, use QID e log source com cuidado, ou extraia propriedade customizada tipada.

```sql
SELECT starttime, LOGSOURCENAME(logsourceid) AS log_source,
       username, sourceip, "EventID"
FROM events
WHERE "EventID" = '4720'
LAST 24 HOURS
```

O resultado depende do DSM, propriedade e fonte. AQL seleciona dados da Ariel; as [instruções IBM de SELECT e AQL](https://www.ibm.com/docs/en/qradar-on-cloud?topic=structure-select-statement) explicam campos, WHERE e janela.

### Elastic Stack, Query DSL

Assume integração Windows em ECS e `winlog.event_id` como keyword.

```json
GET logs-windows.security-*/_search
{
  "query": {
    "bool": {
      "filter": [
        { "term": { "winlog.event_id": "4720" } },
        { "range": { "@timestamp": { "gte": "now-24h" } } }
      ]
    }
  },
  "_source": ["@timestamp", "host.name", "user.name", "winlog.event_data"]
}
```

Troque o padrão de índice e confira mapping/campos. A [integração Windows da Elastic](https://www.elastic.co/guide/en/integrations/current/windows.html/) descreve os campos `winlog.*` disponíveis.

### Wazuh Rules

Assume Windows EventChannel decodificado por Wazuh e `win.system.eventID` disponível. Em Wazuh, uma regra local normalmente herda o decoder e o contexto de uma regra base com `<if_sid>`. Como esse identificador depende da versão e do conjunto de regras instalado, descubra-o com `wazuh-logtest` usando um evento 4720 sintético ou autorizado e consulte a regra base indicada antes de copiar o exemplo. Substitua `ID_DA_REGRA_BASE` por esse identificador real. O exemplo não pode ser carregado enquanto o marcador estiver presente.

```xml
<group name="local,windows,account_management,">
  <rule id="100472" level="5">
    <if_sid>ID_DA_REGRA_BASE</if_sid>
    <field name="win.system.eventID">^4720$</field>
    <description>Lab: Windows user account creation event observed</description>
    <options>no_full_log</options>
  </rule>
</group>
```

Confirme se sua versão extrai o campo, se a regra base é a correta e se o XML é aceito pelo decoder antes de reiniciar o manager. Teste primeiro com `wazuh-logtest`; siga o procedimento de validação indicado pela documentação da sua versão. Consulte [sintaxe das regras Wazuh](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/index.html), [campos e regras](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html) e [coleta Windows EventChannel](https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/configuration.html).

## Mapping ATT&CK

O comportamento de conta criada é candidato a `T1136`. `T1136.001` só faz sentido se o objeto criado estiver confirmado como conta local. No Lab 02, numa VM não associada a domínio, o contexto controlado pode justificar esse mapping local. Um Event ID 4720 isolado em ambiente de função desconhecida não diferencia `.001`, `.002` ou intenção.

ATT&CK descreve comportamento; o evento Windows é evidência possível. Registre domínio, versão, data e a fonte da decisão em [ATT&CK na prática](../lab-12-mitre/README.md).

## Teste da lógica

| Caso | Resultado esperado |
| --- | --- |
| 4720 de conta descartável local no lab | Retornado para revisão com autor e alvo. |
| 4624 de login bem-sucedido | Não retorna. |
| 4720 sem campo de alvo após parsing | Detectar campo ausente e abrir gap de parsing, não inventar identidade. |
| Sem evento no SIEM | Conferir origem, auditoria, ingestão e intervalo antes de concluir. |

## Entrega

Salve sua query/regra num arquivo local, registre pressupostos do schema, exemplos positivos e negativos, evidência anonimizada, falsos positivos, campos ausentes e limitações. Não chame a regra de cobertura geral de `T1136`.
