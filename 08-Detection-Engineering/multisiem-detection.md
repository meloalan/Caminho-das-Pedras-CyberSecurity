# Uma especificação de conta criada, quatro implementações

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](testing-detections.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](sigma.md)

## Especificação comum

**DET-WIN-ACCOUNT-001, experimental:** produzir um candidato de triagem para cada criação de conta Windows observada no contrato de fonte. Seleção: Security-Auditing, canal Security, 4720. Entrega: ator e autoridade, alvo e autoridade, host, horário e identificador do evento quando disponível. Contexto ausente é sinalizado; não prova legitimidade nem ameaça.

A finalidade é conferir autorização e atividade posterior. O piloto só avança quando a fonte, a fila, o volume e o runbook forem validados. O [YAML educacional](../detections/windows/account-management/DET-WIN-ACCOUNT-001.yml) não é formato de importação em SIEM.

## Conceitos relacionados, mecanismos diferentes

| Conceito | Sentinel | Splunk | QRadar | Wazuh |
| --- | --- | --- | --- | --- |
| Pesquisa | KQL | SPL | AQL | Dashboard/indexer; WQL em contextos próprios |
| Regra | Analytics Rule | Saved search com alert; correlation search no ES | CRE Rule | Regra no servidor |
| Agrupamento operacional | Incident conforme configuração/produto | Alert no Enterprise; recursos do ES dependem da versão | Offense conforme resposta/indexação | Alertas e integrações; sem equivalente obrigatório a Incident/Offense |
| Automação | Automation Rules e integrações com Logic Apps | Alert actions e integrações; SOAR se adotado | Respostas e integrações configuradas | Active Response e integrações |

Não há automação de contenção habilitada neste exercício. Não há escala comum entre Wazuh level, severidade de alerta e magnitude de offense.

## Sentinel: query mais configuração

Use a [query de conta criada](../queries/account-creation/README.md) após validar SecurityEvent. Ela tem uma data fixa para investigação histórica. Para uma Analytics Rule agendada de laboratório, substitua a janela fixa por uma janela compatível com o agendamento, como este recorte de implementação:

```kusto
SecurityEvent
| where TimeGenerated >= ago(10m)
| where EventID == 4720
| project TimeGenerated, Computer, EventID,
    SubjectUserName, SubjectDomainName,
    TargetUserName, TargetDomainName, TargetSid
```

O filtro pressupõe o contrato de coleta de SecurityEvent para esses eventos Windows. Execute a cada cinco minutos e pesquise dez minutos apenas como configuração didática inicial. Threshold de resultados maior que zero; mapeie host e contas, preservando ator e alvo separados. Escolha agrupamento e criação de incidentes conforme a versão e o fluxo do SOC. Sobreposição pode repetir candidatos; teste agrupamento/deduplicação, limites e atraso real. O atraso embutido do scheduler não substitui medição da ingestão.

## Splunk: Enterprise e ES são contextos distintos

Parta da [query SPL do catálogo](../queries/account-creation/README.md), com extrações e aliases validados. Uma saved search pode produzir alert no Splunk Enterprise sem Enterprise Security. Correlation search, notables/findings e fluxos de investigação dependem do ES e da sua versão.

```spl
index=windows source="XmlWinEventLog:Security" EventCode=4720 earliest=-10m latest=now
| table _time EventCode lab_host lab_actor lab_user lab_domain
```

O índice/source e aliases são contrato do laboratório, não padrões universais. Acrescente autoridade do ator, SID e identificador original às extrações antes de declarar o alerta completo. Agendamento didático a cada cinco minutos, condição número de resultados maior que zero e ação de revisão manual. Confira scheduler, permissões, busca por event time, sobreposição e throttling. Supressão ampla por host pode ocultar contas novas diferentes.

## QRadar: pesquisa AQL não é regra CRE

Use a [query AQL](../queries/account-creation/README.md) para verificar amostra e propriedades Lab* configuradas no DSM. O CRE avalia testes sobre eventos/flows conforme seu mecanismo; não basta colar SELECT na interface e chamá-lo de regra.

Na configuração conceitual, restrinja log source apropriado, confirme evento normalizado/QID ou propriedade do ID original, provedor e canal, e exija 4720. Um building block pode reutilizar a seleção de fontes, mas não produz resposta por si só. A regra define resposta, contexto e criação/indexação de offense quando desejada. Escolha chave que preserve a identidade alvo, trate propriedade nula e teste coalescência. Não use QID 4720: QID e Windows Event ID são identificadores diferentes.

## Wazuh: regra no servidor, busca no indexer

A amostra especializa a regra nativa 60109 do ruleset Wazuh 4.14, que reconhece criação ou habilitação de conta; o filtro 4720 restringe a criação. O if_sid depende dessa regra e da cadeia nativa do decoder windows_eventchannel. Confira o ruleset instalado antes de usar esse ID.

O [XML didático](../detections/windows/account-management/wazuh-account-created.xml) usa campos do decoder nativo Windows EventChannel. IDs customizados devem ser únicos no ambiente. A amostra escolhe 100820, mas o operador precisa verificar colisões antes de instalar.

```xml
<group name="local,windows,account_management,">
  <rule id="100820" level="8">
    <if_sid>60109</if_sid>
    <field name="win.system.providerName">^Microsoft-Windows-Security-Auditing$</field>
    <field name="win.system.channel">^Security$</field>
    <field name="win.system.eventID">^4720$</field>
    <description>LAB: Windows account created; verify authorization</description>
  </rule>
</group>
```

Level 8 é valor didático, não avaliação universal de risco. Confira saída do decoder e regras nativas já existentes antes de adicionar outra: IDs diferentes podem detectar o mesmo comportamento. Teste a regra com wazuh-logtest no laboratório e verifique a regra efetivamente selecionada, campos, nível e entrega do alerta. XML bem formado localmente não é prova dessa execução.

`frequency`, `timeframe`, `if_matched_sid` e `same_field` podem formar correlações específicas no servidor, com estado e restrições próprios. Não são um join arbitrário entre documentos históricos do indexer. Não crie decoder novo se o nativo já entrega o contrato necessário. Active Response não é solicitado aqui.

## Prova de equivalência de intenção

Em cada produto, uma criação autorizada e uma não explicada correspondem à baseline; 4624 não corresponde; campo de ator ausente deve ser visível como falha de contexto. Registre diferenças de relógio, normalização, contagem, deduplicação e agrupamento. Os mecanismos não serão equivalentes em todos esses aspectos.

As [fontes oficiais das quatro plataformas](referencias.md) sustentam os exemplos. Execução de KQL/SPL, CRE e wazuh-logtest permanece tarefa de integração em ambiente real de laboratório.

## Checkpoint

**Uma consulta AQL que retorna 4720 já configura uma regra CRE?**

<details>
<summary>Ver resposta</summary>

Não. Ela valida pesquisa histórica e propriedades. A regra CRE exige seus testes, condições, estado e respostas configurados e validados separadamente.

</details>

[← Tópico anterior](testing-detections.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](sigma.md)
