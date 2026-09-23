# 12 — Labs práticos

[← Voltar para página principal](../README.md)

Os seis roteiros estão disponíveis; nenhum resultado real é alegado. Comece localmente pelos Labs 01–03. Para executar suas queries no SIEM, faça o Lab 05 antes da etapa KQL. Depois avance para correlação e hunting.

| Lab | Foco | Status |
| --- | --- | --- |
| [Lab 01 — Falhas de autenticação (4625)](01-EventID-4625/README.md) | Investigar uma falha de autenticação Windows sem assumir que ela é maliciosa. | Roteiro; evidências pendentes |
| [Lab 02 — Criação de usuário (4720)](02-EventID-4720/README.md) | Identificar criação de conta e distinguir ator, alvo e escopo local. | Roteiro; evidências pendentes |
| [Lab 03 — Sysmon Process Creation](03-Sysmon-EventID-1/README.md) | Relacionar processo, pai e linha de comando usando Event ID 1 do Sysmon. | Roteiro; evidências pendentes |
| [Lab 04 — Falhas seguidas de login com sucesso](04-BruteForce-Login-Sucesso/README.md) | Correlacionar falhas anteriores a um sucesso sem confundir ordem, conta ou origem. | Roteiro; evidências pendentes |
| [Lab 05 — Coleta e investigação no Sentinel](05-Microsoft-Sentinel/README.md) | Montar e verificar o caminho entre evento Windows e consulta no workspace. | Roteiro; evidências pendentes |
| [Lab 06 — Hunt baseado em hipótese](06-Threat-Hunting/README.md) | Testar se relações pouco frequentes de PowerShell precisam de investigação adicional. | Roteiro; evidências pendentes |

Use o [template](TEMPLATE-LAB.md) para novos relatos e o [catálogo KQL](../queries/kql/README.md) para consultar lógica e limitações. Nunca simule evidência de execução: mantenha resultado esperado separado do obtido.
