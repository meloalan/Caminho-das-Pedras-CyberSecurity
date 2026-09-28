# Referências e limites da validação

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](exemplo-hunt-completo.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](labs/README.md)

## Windows Security Auditing

As páginas oficiais descrevem versão, campos e condições de geração. Confirme a política e o schema instalado antes de executar. Event ID não é prova de intenção.

| Evento | Significado usado |
| --- | --- |
| [4624](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624) | Logon bem-sucedido |
| [4625](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625) | Falha de logon |
| [4648](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4648) | Tentativa de uso de credenciais explícitas |
| [4672](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4672) | Privilégios especiais atribuídos a novo logon |
| [4688](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688) | Processo criado |
| [4697](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4697) | Serviço instalado |
| [4698](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4698) | Tarefa agendada criada |
| [4720](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4720) | Conta criada |
| [4722](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4722) | Conta habilitada |
| [4723](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4723) | Tentativa de troca de senha |
| [4724](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4724) | Tentativa de reset de senha |
| [4732](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4732) | Membro adicionado a grupo local de segurança |
| [4738](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4738) | Conta alterada |
| [4740](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4740) | Conta bloqueada |
| [4768](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4768) | Solicitação de TGT Kerberos |
| [4769](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4769) | Solicitação de ticket de serviço Kerberos |
| [4771](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4771) | Falha de pré-autenticação Kerberos |
| [4776](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4776) | Tentativa de validação de credenciais |
| [1102](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-1102) | Security Log limpo |

4728 e 4756 são adições a grupos global/universal de segurança; consulte [Audit Security Group Management](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-security-group-management). A autoridade do grupo e seus direitos efetivos precisam de contexto.

## Sysmon e ATT&CK

- [Sysmon oficial](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon): IDs 1, 3, 7, 8, 10, 11, 12, 13, 14 e 22. Os fixtures utilizam somente 1, 3 e 22.
- [Técnicas e aplicação local](hunting-with-attack.md): links oficiais para os mappings candidatos.
- [ATT&CK v18](https://attack.mitre.org/resources/updates/updates-october-2025/): mudança de estrutura defensiva e depreciação de Data Sources.
- [Detection Strategies](https://attack.mitre.org/detectionstrategies/): referência atual, sem presumir implementação local.
- [Pyramid of Pain, David Bianco/SANS](https://www.sans.org/tools/the-pyramid-of-pain): modelo conceitual, não lei universal.

## Consultas e cobertura de plataformas

- [Schema SecurityEvent](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityevent) e [KQL project](https://learn.microsoft.com/en-us/kusto/query/project-operator).
- [Splunk: time modifiers](https://help.splunk.com/en/splunk-enterprise/spl-search-reference/10.2/time-format-variables-and-modifiers/time-modifiers) e [sort](https://help.splunk.com/en?resourceId=Splunk_SearchReference_Sort&version=splunk-9_4).
- [IBM: exemplos AQL](https://www.ibm.com/docs/en/qsip/7.5.0?topic=structure-sample-aql-queries) e [guia AQL](https://www.ibm.com/docs/SS42VS_7.4/com.ibm.qradar.doc/b_qradar_aql.pdf). Conferir versão e fuso instalados.
- [Wazuh: event logging](https://documentation.wazuh.com/current/user-manual/manager/event-logging.html), [índices](https://documentation.wazuh.com/current/user-manual/wazuh-indexer/wazuh-indexer-indices.html) e [API do indexer](https://documentation.wazuh.com/current/user-manual/indexer-api/index.html).
- [OpenSearch: busca e filtros](https://docs.opensearch.org/latest/getting-started/search-data/) e [range](https://docs.opensearch.org/latest/query-dsl/term/range/). A documentação latest não garante todos os recursos de outra versão do indexer.

## Revisão e reprodução

Conferência documental em 28/09/2026. Os exemplos KQL, SPL, AQL e DSL têm contratos declarados, mas não foram executados em tenants/instâncias reais. A validação local cobre arquivos, links, cálculos dos fixtures, Markdown, SVG e Mermaid. Parsing ou renderização não comprovam ingestão, permissão, completude ou equivalência entre produtos.

Os módulos [07](../07-Buscas-e-Queries-em-SIEM/README.md) e [08](../08-Detection-Engineering/README.md) mantêm sintaxe detalhada e engenharia operacional. Este módulo reutiliza seus conceitos sem replicar catálogos inteiros.

## Checkpoint

**Qual validação ainda depende do ambiente?**

<details>
<summary>Ver resposta</summary>

Schema, coleta, retenção, permissões, execução de queries, limites de exportação, correlação e operação. Revisão documental e dados fictícios não substituem esses testes.

</details>

[← Tópico anterior](exemplo-hunt-completo.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](labs/README.md)
