# Telemetria: contrato, cobertura e lacunas

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](detection-lifecycle.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-types.md)

> Não é possível detectar aquilo que não conseguimos observar. Ausência de evento também pode ser ausência de coleta.

## Contrato antes da lógica

| Verificação | Evidência a coletar | Se falhar |
| --- | --- | --- |
| Fonte e política de auditoria | Evento original de uma ação autorizada | Corrigir auditoria antes da query |
| Agente e coleta | Mesmo registro na origem e no destino | Investigar transporte e filtros |
| Parser | Campos do payload comparados à extração | Registrar parser e versão |
| Tipos e semântica | Ator, alvo, host, SID e horário identificados | Não correlacionar entidades ambíguas |
| Tempo | Horário original, ingestão, UTC e atraso medido | Ajustar teste de janela e atraso |
| Perda e duplicação | IDs, contagens e amostras por fonte | Medir cobertura e deduplicação |
| Retenção | Período disponível para baseline e investigação | Limitar a hipótese ao histórico existente |
| Implantação | Inventário de ativos esperados e observados | Abrir lacuna com responsável |

## Campos do 4720

No evento original, SubjectUserName/SubjectDomainName representam quem solicitou a criação; TargetUserName/TargetDomainName e TargetSid representam a conta criada. Computer indica onde o evento foi gerado. System/TimeCreated carrega o horário original; TimeGenerated é o nome utilizado na tabela SecurityEvent do exemplo KQL.

Campos `actor`, `user`, `domain` e `timestamp` dos fixtures são nomes didáticos. SPL pode usar aliases; AQL pode exigir propriedades DSM; no Wazuh os campos decodificados começam com `win.*`, enquanto documentos indexados podem apresentá-los em `data.win.*`. Não copie nomes entre camadas sem conferir o registro.

## Telemetry gap documentado

| Lacuna fictícia | Consequência | Tratamento e dono |
| --- | --- | --- |
| WIN-LAB03 sem coleta confirmada | Nenhuma conclusão sobre atividade nesse host | Equipe LAB de coleta deve conferir inventário e agente |
| CommandLine ausente em 4688 | Lógica baseada em argumentos não é avaliável | Verificar política de inclusão de linha de comando |
| Apenas dois dias de retenção | Baseline de mês não pode ser calculado | Reduzir escopo ou ampliar retenção |
| SubjectUserName vazio em um 4720 | Ator não pode ser validado pelo campo extraído | Preservar sinal e registrar falha de contexto |

Uma lacuna deve ter fonte, campo, população afetada, evidência, risco, owner e condição para reavaliar. Não invente valores para preencher campos obrigatórios. No avaliador local, evento 4720 com ator nulo ainda corresponde à seleção, mas recebe aviso de contexto ausente.

## Auditoria por comportamento

Account Management sustenta criação de conta; Security Group Management sustenta alterações de membros; Logon e Special Logon apoiam sessão e privilégios; Process Creation depende da auditoria adequada. Sysmon tem configuração própria e não deve ser presumido em todos os hosts. O Event ID 3 de rede pode não estar habilitado.

Consulte a [matriz de eventos e fontes](referencias.md) e o [contrato do módulo 07](../07-Buscas-e-Queries-em-SIEM/campos-e-schemas.md). A arquitetura de coleta está no módulo 06, sem repetição aqui.

## Checkpoint

**Um 4720 sem ator deve desaparecer da detecção?**

<details>
<summary>Ver resposta</summary>

Não silenciosamente. O comportamento ainda foi observado; preserve o candidato, registre contexto incompleto e trate a qualidade da fonte. Correlações que exigem o ator devem declarar a lacuna.

</details>

[← Tópico anterior](detection-lifecycle.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](detection-types.md)
