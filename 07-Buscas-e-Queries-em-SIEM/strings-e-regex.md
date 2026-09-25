# Strings, caminhos e regex com contexto

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](operadores-e-transformacoes.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](tempo-em-queries.md)

## O que significa “contém PowerShell”?

Igualdade de nome, substring de caminho e termo tokenizado são perguntas diferentes. Primeiro confirme o campo Image, o tipo e a amostra. Um comando pode citar PowerShell sem que ele seja o executável observado.

| Intenção | KQL | SPL em where | AQL | Query DSL sobre keyword |
| --- | --- | --- | --- | --- |
| Igualdade exata | ==; =~ ignora caixa | = compara; normalize conscientemente | =; conferir caixa | term, sensível ao valor indexado |
| Contém substring | contains / contains_cs | like(campo,"%texto%") | ILIKE / LIKE '%texto%' | wildcard *texto* |
| Começa com | startswith / startswith_cs | like(campo,"texto%") | LIKE 'texto%' | prefix ou wildcard texto* |
| Termina com | endswith / endswith_cs | like(campo,"%texto") | LIKE '%texto' | wildcard *texto |
| Regex | matches regex | match() / rex para extração | MATCHES / IMATCHES | regexp sobre termos |

KQL `has` testa termos, não é sinônimo de contains. `text` analisado no indexer é diferente de keyword. SPL `search campo="*texto*"` não é a mesma expressão de `where like(...)`. AQL usa `%`; Query DSL wildcard usa `*` e `?`. Escaping deve respeitar também a string que contém o padrão, como JSON ou SPL.

## A mesma pesquisa nas quatro abordagens

Contrato: [campos e schemas](campos-e-schemas.md). JSON é API do indexer em archives. `case_insensitive` precisa ser suportado na versão instalada; wildcard inicial pode ser caro ou bloqueado por configuração.
<details>
<summary>Ver consulta em KQL</summary>

```kusto
WindowsEvent
| where TimeGenerated >= ago(24h)
| where Provider == "Microsoft-Windows-Sysmon" and EventID == 1
| extend Image=tostring(EventData.Image), ParentImage=tostring(EventData.ParentImage), CommandLine=tostring(EventData.CommandLine)
| where Image contains "powershell"
| project TimeGenerated, Computer, Image, ParentImage, CommandLine
```

</details>

<details>
<summary>Ver consulta em SPL</summary>

```spl
index=windows source="XmlWinEventLog:Microsoft-Windows-Sysmon/Operational" earliest=-24h latest=now EventCode=1
| where like(lower(lab_image), "%powershell%")
| table _time lab_host lab_user lab_image lab_parent lab_command
```

</details>

<details>
<summary>Ver consulta em AQL</summary>

```sql
SELECT starttime, "LabComputer", "LabUser", "LabImage", "LabParent", "LabCommand"
FROM events
WHERE "LabProvider" = 'Microsoft-Windows-Sysmon' AND "LabEventID" = '1'
AND "LabImage" ILIKE '%powershell%'
ORDER BY starttime ASC LIMIT 50
LAST 24 HOURS
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
              "gte": "now-24h",
              "lt": "now"
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
        },
        {
          "wildcard": {
            "data.win.eventdata.image": {
              "value": "*powershell*",
              "case_insensitive": true
            }
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

O filtro seleciona candidatos com esse trecho no caminho. Um resultado pede pai, usuário, argumentos, host, sessão e finalidade. Uma ferramenta administrativa ou LOLBin não vira ameaça pelo nome. No dataset, PowerShell aparece com pais diferentes e comandos benignos; compare as relações, não só o executável.

## Regex mínima e testável

Um literal procura texto; `.` numa regex representa qualquer caractere, enquanto `\.` representa ponto literal. Parênteses podem capturar grupos; alternativas usam `|` na regex. Isso não é o pipe externo do KQL/SPL. Uma regex aceita por um produto pode falhar em outro: mecanismos e suporte a lookarounds/backreferences diferem. Regexp de OpenSearch opera sobre termos e não deve ser tratada como PCRE universal.

Use regex para uma extração que padrões simples não resolvem. Teste correspondência esperada, caixa diferente, separadores, campo vazio, caminho parecido e string longa. Preserve o texto original. Comece por dataset/tempo/filtros seletivos, depois avalie custo e completude.

## Referências

- [Operadores de strings KQL](https://learn.microsoft.com/en-us/kusto/query/datatypes-string-operators).
- [Operadores AQL](https://www.ibm.com/docs/en/qsip/7.5.0?topic=language-aql-logical-comparison-operators).
- [Wildcard OpenSearch](https://docs.opensearch.org/latest/query-dsl/term/wildcard/).

## Desafio

Compare `powershell.exe`, `PowerShell.EXE` e `powershell-helper.exe`. Explique por que substring encontra os três em uma comparação sem distinção de caixa, mas igualdade do nome completo responde a outra pergunta.

## Checkpoint

**Posso copiar uma regex entre quatro mecanismos?**

<details>
<summary>Ver resposta</summary>

Não sem testar. Sintaxe, escaping, tokenização e recursos variam. Prefira operador simples quando ele expressa a intenção.

</details>

[← Tópico anterior](operadores-e-transformacoes.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](tempo-em-queries.md)
