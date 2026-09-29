# Lab 03: Sysmon e telemetria de endpoint

[← Índice da trilha](../README.md) · [Página principal](../../README.md) · [Lab 02: Logs](../lab-02-logs/README.md) · [Lab 04: SIEM](../lab-04-siem/README.md) · [Roteiro detalhado Event ID 1](../03-Sysmon-EventID-1/README.md)

**Pré-requisito:** Lab 01 e Windows de laboratório. **Status: roteiro.**

## Objetivo

Instalar o Sysmon oficial numa VM Windows descartável, validar os eventos na origem e comparar dados de endpoint com Security log.

## Eventos para reconhecer

| Sysmon ID | Nome | O que pode ajudar a observar |
| --- | --- | --- |
| 1 | Process Create | imagem, processo pai, usuário, ProcessGuid e argumentos quando coletados |
| 3 | Network Connection | conexões TCP/UDP atribuídas a processo, se habilitadas |
| 11 | File Create | criação de arquivo em caminhos observados |
| 13 | Registry Value Set | modificação de valor de registro |
| 22 | DNS Query | consulta DNS vista pelo processo, conforme versão/configuração |

Os eventos 3, 11, 13 e 22 dependem de configuração, versão, filtros e comportamento. Consulte a [lista atual de eventos Microsoft Sysmon](https://learn.microsoft.com/windows/security/operating-system-security/sysmon/sysmon-events). Um canal silencioso pode significar filtro, auditoria, ausência de comportamento ou ingestão quebrada.

## Instalação controlada

1. Restaure ou crie snapshot da VM Windows e anote versão do SO.
2. Baixe o pacote Sysmon somente de [Microsoft Sysinternals](https://learn.microsoft.com/sysinternals/downloads/sysmon).
3. Revise a licença e os parâmetros oficiais; instale apenas no Windows descartável.
4. Sem configuração de terceiros, instale com a opção padrão documentada `sysmon64.exe -accepteula -i` quando a arquitetura for x64. Esse passo é uma instalação persistente até desinstalar ou restaurar snapshot.
5. Abra Event Viewer, Applications and Services Logs, Microsoft, Windows, Sysmon, Operational.
6. Gere comportamento benigno: abra o terminal, rode `Get-Date` e navegue para um site de documentação permitido, se NAT estiver temporariamente ativo.
7. Verifique 1 e, caso a configuração e o filtro registrem, 3 ou 22. Registre a ausência como observação, sem presumir falha.
8. Não habilite captura ampla de rede, não use payloads e não altere a configuração em máquinas corporativas.

## Validar campos

Use detalhes XML para conferir `UtcTime`, `ProcessGuid`, `Image`, `CommandLine`, `ParentImage`, `DestinationIp`, `DestinationPort`, `TargetFilename` ou `QueryName` quando presentes no evento correspondente. Campos variam por Event ID e configuração. `ProcessGuid` é mais adequado que PID isolado para correlação temporal longa, pois PIDs são reutilizados.

## Ingestão no SIEM

O Lab 04 ensina a escolha da plataforma. Registre o nome real do canal e confirme que o coletor o envia. Sentinel pode armazenar Sysmon em WindowsEvent após configuração de DCR. Outras opções incluem Wazuh, Elastic Agent e Splunk Universal Forwarder. Não assuma que o conector Security Events inclui Sysmon automaticamente.

## Limpeza

Se instalou só para este exercício, prefira restaurar `base-limpa`. Alternativamente, use o comando oficial de desinstalação do Sysmon após conferir o sistema alvo. Exporte evidências redigidas antes. Não desinstale o Sysmon de dispositivo gerenciado.

## Entrega

Anote versão do Sysmon, configuração, canal, evento, campos, horário UTC, diferença entre origem e SIEM e limitações. Siga para [montar um SIEM](../lab-04-siem/README.md).
