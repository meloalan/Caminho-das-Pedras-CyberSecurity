# Processos registrados pelo Sysmon

[← Catálogo KQL](README.md) · [Página principal](../../README.md)

## O que procura

Lista criações de processos com imagem, pai e linha de comando.

## Query

[Arquivo executável em KQL](03-sysmon-processos.kql)

```kql
// Pressupõe Sysmon coletado na tabela WindowsEvent com EventData dinâmico.
WindowsEvent
| where TimeGenerated >= ago(24h)
| where Provider == "Microsoft-Windows-Sysmon" and EventID == 1
| extend Image = tostring(EventData.Image), CommandLine = tostring(EventData.CommandLine),
         ParentImage = tostring(EventData.ParentImage), ProcessGuid = tostring(EventData.ProcessGuid)
| project TimeGenerated, Computer, Image, ParentImage, CommandLine, ProcessGuid
| sort by TimeGenerated desc
```

## Como funciona

Provider evita confundir Event ID 1 de outros provedores. `extend` extrai campos do objeto dinâmico e `tostring` estabiliza o tipo. `project` reduz a saída.

## Possíveis false positives

A query é um inventário: praticamente todos os processos legítimos também aparecem. Ela não é um classificador de malware.

## Como melhorar

Conferir o XML e o parser da coleta; se os dados chegam em Event ou outra tabela, adaptar explicitamente. Correlacionar ProcessGuid e contexto, evitando depender apenas do nome.

## Validação

Exemplo educacional, ainda não executado em um workspace real. Confira esquema, provedor, auditoria e intervalo de tempo antes de usar. Resultado vazio também pode indicar falha de coleta.

TODO: adicionar evidência real do laboratório
