# Coleta de logs com propósito

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](log-pipeline.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](parsing-normalizacao.md)

## Escolher a fonte pela pergunta

Para investigar autenticação Windows, consulte Security no host ou DC que processou a operação. Para um login cloud, procure a fonte de identidade correspondente. O mesmo nome de usuário em dois serviços não cria automaticamente uma chave de correlação.

| Fonte | Pergunta possível | Pré-requisito e limite |
| --- | --- | --- |
| Windows Security | Quem autenticou ou criou uma conta? | Subcategoria de auditoria e canal corretos |
| Sysmon | Qual processo iniciou e qual seu pai? | Configuração de eventos e sensor ativo |
| Linux | Que autenticação, serviço ou ação foi registrada? | journald/arquivos/audit conforme distribuição e configuração |
| Firewall/proxy/DNS | Que comunicação ou resolução foi observada? | Visibilidade, protocolo e tratamento de NAT |
| Entra ID/Microsoft 365 | Que identidade ou operação cloud aparece? | Permissões, integração, produto e retenção |
| Aplicação | Qual operação funcional ocorreu? | Logging da aplicação e identificação de sessão |

## Agente, API, encaminhamento e WEF

Agente lê fontes locais e pode usar buffer. API costuma exigir identidade, paginação, cursor, limites e política de repetição. Encaminhamento centraliza dados, mas precisa preservar o host original. WEF entrega eventos Windows a um WEC; o coletor do SIEM então lê os eventos encaminhados.

| Plataforma | Caminho Windows do laboratório | Primeira validação |
| --- | --- | --- |
| Wazuh | Agent eventchannel → manager → indexer | Evento decodificado e alerta/archive esperado |
| Splunk | Universal Forwarder → indexer → search head | Index, source, sourcetype e campos |
| QRadar | WinCollect/integração → log source → processamento | Payload, DSM, log source e event ID extraído |
| Sentinel | AMA/DCR no caminho suportado → workspace | Associação ao host, canal e tabela |

Os caminhos dependem de sistemas suportados e versões. Não colete o mesmo canal pelo agente e por WEF sem uma estratégia explícita para deduplicar. Não desative validação TLS para facilitar o laboratório.

## Plano de ativação

1. Escolha um host próprio e uma atividade benigna conhecida.
2. Confirme que o evento existe localmente antes de configurar o destino.
3. Revise compatibilidade, permissões, rede e orçamento do ambiente escolhido.
4. Configure um conjunto pequeno de canais com a documentação do produto.
5. Compare o mesmo registro na origem e no SIEM, incluindo identidade e tempo.
6. Meça atraso e verifique que eventos não selecionados permanecem fora do escopo.
7. Registre configuração, versão, responsável, rollback e impacto de retenção.

## Segurança e recuperação

Credenciais de ingestão e consulta têm finalidades diferentes. Separe privilégios e mantenha segredos fora de exemplos versionados. Planeje o que acontece durante falha de rede: tamanho do buffer, perda, reenvio, duplicação e chegada tardia variam por agente e protocolo.

Uma integração sem responsável tende a ficar esquecida quando o schema muda. Defina revisão por mudança de versão, não apenas por calendário. Remova recursos exclusivos do lab ao terminar, preservando as notas e verificando custos remanescentes.

## Prática

Entregue um contrato com canal, provedor, IDs, intervalo, destino, campos obrigatórios e critérios de aceitação. Para cada plataforma, identifique o componente que executaria a coleta. Use a [página Sysmon/WEF](sysmon-wef.md) para diferenciar canal de origem e canal encaminhado.

## Referências para configurar

- [Coleta Wazuh](https://documentation.wazuh.com/current/user-manual/capabilities/log-data-collection/configuration.html): canais e formato eventchannel.
- [Microsoft: conectores Windows](https://learn.microsoft.com/en-us/azure/sentinel/connect-services-windows-based): pré-requisitos e destinos SecurityEvent/WindowsEvent.
- [Splunk Windows add-on](https://splunk.github.io/splunk-add-on-for-microsoft-windows/): configuração e campos da integração.
- [IBM WinCollect](https://www.ibm.com/docs/en/qradar-common?topic=10-wincollect-overview): caminhos Windows e requisitos do coletor.

## Checkpoint

**É correto começar pela regra antes de confirmar a fonte?**

<details>
<summary>Ver resposta</summary>

Você pode especificar a intenção, mas não declarar a regra funcional sem validar a telemetria necessária.

</details>

**WEF substitui o SIEM?**

<details>
<summary>Ver resposta</summary>

Não. Encaminha eventos para um coletor Windows; armazenamento investigativo e detecção dependem do restante da arquitetura.

</details>

[← Tópico anterior](log-pipeline.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](parsing-normalizacao.md)
