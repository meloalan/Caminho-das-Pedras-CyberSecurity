# Lab 03 — Sysmon Process Creation

[← Índice dos labs](../README.md) · [← Voltar para página principal](../../README.md)

**Status: roteiro introdutório; execução e evidências pendentes.**

## Objetivo

Relacionar processo, pai e linha de comando usando Event ID 1 do Sysmon.

## Cenário

Execução benigna de `powershell.exe -NoProfile -Command "Get-Date"` em VM.

## Arquitetura

VM Windows em rede de laboratório → canal de eventos local → agente/regra de coleta, quando configurados → Log Analytics/Sentinel. Os Labs 01–03 podem começar apenas pelo Event Viewer; KQL exige fonte correspondente. Nenhum ambiente foi provisionado por este repositório.

## Pré-requisitos

Administração local; Sysmon oficial instalado com configuração revisada que inclua ProcessCreate; conferir se filtros excluem o processo. Para KQL, coletar o canal operacional para WindowsEvent conforme Lab 05.

## Ferramentas utilizadas

Windows, Event Viewer e PowerShell; Sysmon quando aplicável; Microsoft Sentinel/Log Analytics para KQL. Registrar versões reais ao executar.

## Execução

1. Registre versão e configuração do Sysmon e faça snapshot antes de instalar ou alterar o sensor.
2. Confirme o canal Microsoft-Windows-Sysmon/Operational.
3. Execute o comando benigno do cenário a partir de um terminal e anote o horário.
4. Filtre EventID 1 do provedor Sysmon; examine Image, ParentImage, CommandLine e ProcessGuid.
5. Compare XML com EventData no SIEM e documente diferenças. Reverta mudanças no sensor somente se ele foi instalado para este exercício.

## Logs gerados

Microsoft-Windows-Sysmon/Operational, provedor Microsoft-Windows-Sysmon, EventID 1.

## Evidências

TODO: adicionar evidência real do laboratório

Guardar XML/EVTX bruto fora do Git; publicar somente campos e capturas anonimizados, com horário e contexto.

## Investigação

Confirme provedor, janela UTC e entidade. Separe ator de alvo e evento de interpretação. Procure explicação legítima; documente campos ausentes, perda de coleta e o que os dados não provam.

## Query

[Query e explicação](../../queries/kql/03-sysmon-processos.md) · [Arquivo KQL](../../queries/kql/03-sysmon-processos.kql). Inclui intenção, operadores, falsos positivos e melhorias.

## Regra de detecção

Inventário de processos; não alertar para todos os EventID 1. Para detecção, escolher uma relação pai/filho e contexto específico e testar comportamento benigno.

## MITRE ATT&CK

Process Creation genérico não determina uma técnica. O comando deste roteiro executa PowerShell, relacionado a [T1059.001](https://attack.mitre.org/techniques/T1059/001/), sem indicar intenção maliciosa.

## Resultado esperado

Localizar o comando benigno e relacionar processo pai e filho. Um EventID 1 de outro provedor não deve ser incluído.

## Resultado obtido

Não executado. TODO: adicionar evidência real do laboratório

## O que aprendi

Preencher após executar: qual hipótese mudou, qual campo foi decisivo e qual limitação permaneceu. TODO: adicionar evidência real do laboratório

## Possíveis melhorias

Validar parser, normalização de contas, deduplicação, atraso e baseline. Expandir somente após confirmar o cenário mínimo.

## Próximos passos

Concluir limpeza descrita na execução, registrar resultado real e revisar a detecção com o [template](../../08-Detection-Engineering/TEMPLATE-DETECCAO.md).
