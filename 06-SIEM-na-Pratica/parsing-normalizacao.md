# Parsing, normalização e enriquecimento

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](coleta-de-logs.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](query-languages.md)

## Três trabalhos diferentes

Parsing extrai estrutura e tipos. Normalização alinha significados. Enriquecimento adiciona contexto de outra fonte. Extrair `src_ip` não comprova que seja o cliente original: pode ser proxy, NAT ou dispositivo que encaminhou o log.

| Representação | Pode significar | Pergunta antes de mapear |
| --- | --- | --- |
| `src_ip`, `source.ip`, `SourceIp` | Origem da comunicação registrada | É cliente, proxy ou endereço traduzido? |
| `sourceAddress`, `client_ip` | Endereço observado pela aplicação | Como o campo foi preenchido? |
| `user`, `Account`, `TargetUserName` | Identidades com papéis diferentes | É ator, alvo ou identidade autenticada? |
| `host`, `Computer`, `agent.name` | Host original ou coletor | Qual máquina realizou a atividade? |

Preserve domínio/autoridade e SID quando disponível. `lab-user` local em duas máquinas não é necessariamente a mesma identidade. No 4720, Subject indica o ator e Target indica a conta criada; fundir ambos num campo `user` destrói uma relação essencial.

## Um mesmo log nos quatro ambientes

Esta representação é **normalizada e fictícia**, não o formato de exportação nativo de nenhum produto:

```json
{
  "timestamp": "2026-09-20T21:30:00Z",
  "provider": "Microsoft-Windows-Security-Auditing",
  "event_id": 4625,
  "user": "lab-user",
  "host": "WIN-LAB01",
  "source_ip": "192.0.2.25",
  "logon_type": 3,
  "status": "0xC000006D",
  "substatus": "0xC000006A"
}
```

O evento representa falha de logon. O código e substatus ajudam a entender a falha, mas não demonstram intenção. Confirme a versão do evento, o contexto do logon e a fonte.

| Intenção | Wazuh eventchannel | Splunk neste lab | QRadar neste lab | Sentinel SecurityEvent |
| --- | --- | --- | --- | --- |
| Event ID | `data.win.system.eventID` | `EventCode` | `LabEventID` | `EventID` |
| Usuário alvo | `data.win.eventdata.targetUserName` | `lab_user` | `LabUser` | `TargetUserName` |
| Host original | `data.win.system.computer` | `lab_host` | `LabComputer` | `Computer` |
| IP observado | `data.win.eventdata.ipAddress` | `lab_source_ip` | `LabSourceIP` | `IpAddress` |
| Tipo de logon | `data.win.eventdata.logonType` | `lab_logon_type` | `LabLogonType` | `LogonType` |
| Domínio alvo | `data.win.eventdata.targetDomainName` | `lab_domain` | `LabDomain` | `TargetDomainName` |

**Os nomes `lab_*` e `Lab*` são contratos explícitos deste exercício, não campos nativos garantidos.** Splunk exige extrações/aliases validados; QRadar exige propriedades personalizadas habilitadas para a fonte e pesquisa. Antes de executar consultas, siga [linguagens](query-languages.md) e [QRadar](qradar.md). Se o dado não existir, registre lacuna; não crie um valor apenas para satisfazer a regra.

## Modelos e mecanismos

Splunk CIM define convenções e modelos usados por conteúdos compatíveis. Add-ons e conhecimento de busca precisam mapear a fonte corretamente. ASIM oferece schemas e parsers de normalização para cenários do Sentinel, inclusive normalização em tempo de consulta. DSM do QRadar reconhece e normaliza eventos, com propriedades adicionais quando necessário. Decoders do Wazuh extraem dados para o mecanismo de análise. Não são quatro nomes para a mesma implementação.

## Contrato para pesquisa reproduzível

Registre campo original, campo de pesquisa, tipo, papel, valores ausentes, transformação e amostra de teste. No Splunk do lab, `lab_user` significa TargetUserName de autenticação; para criação de conta, mantenha também `lab_actor`. Em QRadar, o tipo texto de LabEventID corresponde às comparações com strings nas consultas AQL deste módulo.

Para Wazuh, confira mapping ou field capabilities antes de usar `term` e agregações `terms`. Um campo `text` analisado e um `keyword` não se comportam da mesma forma. O sufixo `.keyword` não deve ser acrescentado por hábito; só use se existir no mapping.

## Erros que mudam conclusões

| Erro | Consequência | Teste |
| --- | --- | --- |
| Trocar ator e alvo | Acusar a conta recém-criada de criar a si mesma | Comparar Subject/Target ao original |
| Converter IP ausente em 0.0.0.0 | Unir atividades sem origem conhecida | Preservar ausência explicitamente |
| Usar nome do coletor como host | Misturar endpoints em WEF | Comparar Computer original |
| Perder offset do timestamp | Inverter sequência | Comparar UTC e valor original |
| Inventário antigo | Priorizar ativo pela função errada | Versionar enriquecimento |

## Prática

Mapeie o JSON acima para sua plataforma. Acrescente um campo de ator apenas se a fonte o sustentar. Mostre um registro antes/depois e explique como provar que a identidade não mudou durante a transformação. A [pedra de Roseta](traduzindo-entre-siems.md) utiliza esse contrato para construir consultas comparáveis.

## Referências

- [Splunk CIM e tipos de fonte](https://splunk.github.io/splunk-add-on-for-microsoft-windows/): relacionamento entre add-on e conhecimento normalizado.
- [ASIM](https://learn.microsoft.com/en-us/azure/sentinel/normalization): schemas e parsers no Sentinel.
- [Schema SecurityEvent](https://learn.microsoft.com/en-us/azure/azure-monitor/reference/tables/securityevent): tipos e campos disponíveis na tabela, cuja população depende do evento.

## Checkpoint

**Por que não unificar todo usuário em um único campo?**

<details>
<summary>Ver resposta</summary>

Ator, alvo e identidade autenticada são papéis diferentes. Preserve relações e autoridade.

</details>

**Normalizar dispensa o dado original?**

<details>
<summary>Ver resposta</summary>

Não. A amostra original ajuda a verificar extrações, investigar regressões e explicar perdas de detalhe.

</details>

[← Tópico anterior](coleta-de-logs.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](query-languages.md)
