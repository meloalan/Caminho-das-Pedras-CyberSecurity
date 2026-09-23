# Hunt de PowerShell

[← Catálogo KQL](README.md) · [Página principal](../../README.md)

## O que procura

Lista as vinte combinações menos frequentes de host, imagem PowerShell e processo pai no período.

## Query

[Arquivo executável em KQL](06-hunt-powershell.kql)

```kql
// Hipótese de triagem: relações pai/filho pouco frequentes merecem contexto.
WindowsEvent
| where TimeGenerated >= ago(7d)
| where Provider == "Microsoft-Windows-Sysmon" and EventID == 1
| extend Image = tostring(EventData.Image), ParentImage = tostring(EventData.ParentImage),
         CommandLine = tostring(EventData.CommandLine)
| where Image endswith @"\powershell.exe" or Image endswith @"\pwsh.exe"
| summarize Executions = count(), FirstSeen = min(TimeGenerated), LastSeen = max(TimeGenerated),
            Examples = make_set(CommandLine, 3) by Computer, Image, ParentImage
| top 20 by Executions asc
```

## Como funciona

Filtra Sysmon 1, extrai EventData, seleciona nomes de imagem e agrega relações pai/filho. `top ... asc` prioriza menor frequência; não existe um limiar de malícia.

## Possíveis false positives

Instalações, suporte técnico, automações novas e tarefas de manutenção.

## Como melhorar

Adicionar baseline por função do host, usuário, assinatura e horário. Binários renomeados não são cobertos. Não publicar linhas de comando sem revisar segredos. T1059.001 descreve PowerShell; uso legítimo também corresponde ao comportamento técnico.

## Validação

Exemplo educacional, ainda não executado em um workspace real. Confira esquema, provedor, auditoria e intervalo de tempo antes de usar. Resultado vazio também pode indicar falha de coleta.

TODO: adicionar evidência real do laboratório
