# Catálogo KQL

[← Voltar para página principal](../../README.md)

Status: exemplos educacionais; validação em Sentinel pendente. Consulte primeiro o esquema da tabela do seu workspace.

| Consulta | Fonte | Uso |
| --- | --- | --- |
| [Falhas de autenticação](01-falhas-autenticacao.md) | SecurityEvent | Estudo e investigação |
| [Criação de conta](02-conta-criada.md) | SecurityEvent | Estudo e investigação |
| [Processos registrados pelo Sysmon](03-sysmon-processos.md) | WindowsEvent / Sysmon | Estudo e investigação |
| [Falhas seguidas de sucesso](04-falhas-seguidas-sucesso.md) | SecurityEvent | Estudo e investigação |
| [Saúde da coleta](05-saude-coleta.md) | SecurityEvent | Estudo e investigação |
| [Hunt de PowerShell](06-hunt-powershell.md) | WindowsEvent / Sysmon | Estudo e investigação |

## Contrato de dados

- [SecurityEvent](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityevent): os exemplos usam TimeGenerated, EventID, Computer e campos normalizados de conta/IP quando aplicável.
- [WindowsEvent](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/windowsevent): Sysmon exige Provider, EventID e EventData com as chaves usadas nas consultas.
- Windows Security Events via AMA, WEF e coleta genérica podem ter destinos e campos diferentes. Não troque apenas o nome da tabela.
- Logs originais e linhas de comando podem conter dados sensíveis. Anonimize qualquer saída publicada.

## Teste sem dados reais

Abra o [exercício sintético](../../07-KQL/fundamentos.md). Ele não exige telemetria e não representa um resultado real do laboratório.
