# ATT&CK como apoio ao raciocínio

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](behavior-based-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](windows-hunting.md)

## Do comportamento à fonte local

Escolha uma técnica relevante para os ativos e o risco. Leia sua descrição e exemplos, transforme em comportamento observável, identifique componentes de dados, telemetria local e campos, formule hipótese e só então escolha consulta.

**Atualização do framework:** Data Sources foram depreciadas no ATT&CK v18. Referências antigas ainda aparecem; consulte as [mudanças oficiais](https://attack.mitre.org/resources/updates/updates-october-2025/) e as [Detection Strategies](https://attack.mitre.org/detectionstrategies/). Não ensine o antigo encadeamento Data Source → Data Component como a única estrutura atual. Estratégias, Analytics e componentes ajudam a organizar a investigação, mas não provam que sua fonte local coleta os campos.

| Referência | Pergunta de hunt | Evidência e limite |
| --- | --- | --- |
| [T1059.001](https://attack.mitre.org/techniques/T1059/001/) | PowerShell participa de uma ação indevida? | Processo, pai, comando e contexto; nome não basta |
| [T1136.001](https://attack.mitre.org/techniques/T1136/001/) / [.002](https://attack.mitre.org/techniques/T1136/002/) | Conta local/domínio foi criada para finalidade indevida? | 4720 e autoridade; investigar uso e autorização |
| [T1098](https://attack.mitre.org/techniques/T1098/) | Mudança de conta/privilégio merece investigação? | Ator, alvo e alteração efetiva, sem mapeamento automático |
| [T1070.001](https://attack.mitre.org/techniques/T1070/001/) | Limpeza de logs está relacionada a ocultação? | 1102 e contexto; manutenção é alternativa |
| [T1053.005](https://attack.mitre.org/techniques/T1053/005/) | Tarefa agendada participa de execução indevida? | 4698, ação, principal, gatilho e execução posterior |
| [T1543.003](https://attack.mitre.org/techniques/T1543/003/) | Serviço foi criado/modificado para abuso? | 4697 e configuração/execução; criação não prova intenção |
| [T1078](https://attack.mitre.org/techniques/T1078/) | Uma identidade válida foi usada indevidamente? | Autenticação e ações corroboradas; sucesso não prova abuso |

## Não mapear além do observado

Uma sequência de falhas e sucesso não comprova brute force, password spray ou credenciais comprometidas. DNS e conexão não provam C2. Mantenha “técnica candidata” quando o propósito não estiver demonstrado e registre qual evidência falta.

## Gaps e cobertura

Para cada hipótese registre fonte esperada, população, campos ausentes e controle positivo. Uma matriz cheia de tags pode esconder coleta inexistente. A [cobertura do módulo 08](../08-Detection-Engineering/coverage.md) oferece o contrato para transformar a hipótese em capacidade validada.

## Checkpoint

**Selecionar T1059 autoriza escolher qualquer Event ID de processo?**

<details>
<summary>Ver resposta</summary>

Não. É preciso traduzir comportamento em campos e conferir que a fonte registra essa manifestação, na população e no período relevantes.

</details>

[← Tópico anterior](behavior-based-hunting.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](windows-hunting.md)
