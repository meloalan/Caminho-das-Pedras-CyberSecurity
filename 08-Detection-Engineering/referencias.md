# Referências e matriz de eventos

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](TEMPLATE-DETECCAO.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](labs/README.md)

## Como usar estas fontes

Referências oficiais conferidas em 28/09/2026. Nomes de telas, versões, schemas e comportamento do agendamento podem mudar. As páginas abaixo sustentam eventos e mecanismos; os valores de limiar, dados e exemplos de operação do módulo são didáticos.

## Windows Security Auditing

Provedor padrão dos eventos abaixo: Microsoft-Windows-Security-Auditing, salvo 1102. Todos são relacionados aqui para conferir contratos usados nos casos e no dataset compartilhado, não como lista automática de regras.

| Evento | Observação registrada | Limite de interpretação |
| --- | --- | --- |
| [4624](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4624) | Logon aceito e sessão criada | Não prova que a autenticação é legítima |
| [4625](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4625) | Falha de logon | Conferir motivo, origem, tipo e contexto |
| [4672](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4672) | Privilégios especiais atribuídos a novo logon | Não equivale a inclusão em grupo ou elevação indevida |
| [4688](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4688) | Criação de processo | Campos dependem de versão e auditoria; command line precisa de configuração |
| [4720](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4720) | Criação de conta de usuário | Confirmar escopo local/domínio e autorização |
| [4728](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-security-group-management) | Membro adicionado a grupo global de segurança | Grupo de domínio; verificar permissões reais |
| [4732](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4732) | Membro adicionado a grupo local de segurança | Confirmar autoridade e contexto do grupo |
| [4740](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4740) | Conta bloqueada | Não identifica sozinho causa adversária |
| [4756](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/audit-security-group-management) | Membro adicionado a grupo universal de segurança | Grupo de domínio; não torna todo grupo privilegiado |
| [4768](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4768) | Solicitação de TGT Kerberos | Conferir resultado e versão; gerado no DC |
| [4769](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4769) | Solicitação de ticket de serviço Kerberos | Não confundir pedido com abuso |
| [4771](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-4771) | Falha de pré-autenticação Kerberos | Conferir código e contexto |
| [1102](https://learn.microsoft.com/en-us/previous-versions/windows/it-pro/windows-10/security/threat-protection/auditing/event-1102) | Limpeza do Security Log | Provedor Microsoft-Windows-Eventlog; contexto continua necessário |

## Sysmon

A [referência oficial Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) descreve 1 (process creation), 3 (network connection), 10 (process access), 11 (file create) e 22 (DNS query). O módulo usa principalmente 1 e o contexto de 3/22 no caso final. 10 e 11 são possibilidades de enriquecimento, não evidências presentes automaticamente no fixture.

Configuração e versão determinam o que é coletado. ProcessGuid ajuda a acompanhar a mesma execução; PID pode ser reutilizado. Hashes e linhas de comando só podem sustentar condições quando disponíveis e completos.

## Plataformas e formatos

- [Sentinel: regras agendadas](https://learn.microsoft.com/en-us/azure/sentinel/scheduled-rules-overview) e [saúde das regras](https://learn.microsoft.com/en-us/azure/sentinel/monitor-analytics-rule-integrity).
- [SecurityEvent, schema](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityevent).
- [Splunk: scheduled alerts](https://help.splunk.com/splunk-cloud-platform/alert-and-respond/alerting-manual/9.2.2406/create-alerts/create-scheduled-alerts) e [correlation searches no ES 7.3](https://help.splunk.com/en/splunk-enterprise-security-7/administer/7.3/correlation-searches/correlation-search-overview-for-splunk-enterprise-security). Confira a versão instalada antes de usar nomenclatura de investigação do ES.
- [QRadar 7.6: CRE, rules e offenses](https://www.ibm.com/docs/en/qsip/7.6.0?topic=phase-qradar-rules-offenses) e [custom rules/building blocks](https://www.ibm.com/docs/en/qradar-on-cloud?topic=siem-custom-rules).
- [Wazuh: sintaxe de regras](https://documentation.wazuh.com/current/user-manual/ruleset/ruleset-xml-syntax/rules.html), [regras customizadas](https://documentation.wazuh.com/current/user-manual/ruleset/rules/custom.html) e [base Windows EventChannel 4.14](https://github.com/wazuh/wazuh/blob/v4.14.0/ruleset/rules/0575-win-base_rules.xml).
- [Sigma specification](https://sigmahq.io/sigma-specification/specification/sigma-rules-specification.html) e [pySigma](https://github.com/SigmaHQ/pySigma).
- [ATT&CK Detection Strategies](https://attack.mitre.org/detectionstrategies/) e [mudanças defensivas do v18](https://attack.mitre.org/resources/updates/updates-october-2025/). Os links de técnicas ficam no [mapeamento](mitre-mapping.md).

## Limites da conferência

Leitura documental e parser local não substituem versão instalada, parser real, logtest, CRE, scheduler ou execução de query. O [catálogo do módulo 07](../queries/README.md) mantém as queries detalhadas e seus contratos. A validação de ambiente deve ser registrada no template, sem apresentar saída esperada como execução realizada.

## Checkpoint

**Por que guardar versão e contrato junto da referência?**

<details>
<summary>Ver resposta</summary>

Porque o mesmo Event ID pode ter versões e campos diferentes, e o SIEM pode normalizar nomes e tipos. A referência descreve a fonte; a validação comprova sua implementação.

</details>

[← Tópico anterior](TEMPLATE-DETECCAO.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](labs/README.md)
