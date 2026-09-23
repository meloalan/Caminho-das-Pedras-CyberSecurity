# Lab 06 — Hunt baseado em hipótese

[← Índice dos labs](../README.md) · [← Voltar para página principal](../../README.md)

**Status: roteiro introdutório; execução e evidências pendentes.**

## Objetivo

Testar se relações pouco frequentes de PowerShell precisam de investigação adicional.

## Cenário

Hipótese: uma relação pai/filho incomum pode revelar execução que merece revisão; hipótese alternativa: tarefa administrativa legítima.

## Arquitetura

VM Windows em rede de laboratório → canal de eventos local → agente/regra de coleta, quando configurados → Log Analytics/Sentinel. Os Labs 01–03 podem começar apenas pelo Event Viewer; KQL exige fonte correspondente. Nenhum ambiente foi provisionado por este repositório.

## Pré-requisitos

Sysmon 1 em WindowsEvent, baseline suficiente para o escopo, campos Image/ParentImage/CommandLine e acesso de leitura. Ausência de baseline torna o resultado exploratório.

## Ferramentas utilizadas

Windows, Event Viewer e PowerShell; Sysmon quando aplicável; Microsoft Sentinel/Log Analytics para KQL. Registrar versões reais ao executar.

## Execução

1. Defina hosts, sete dias de dados e critérios de encerramento.
2. Verifique coleta com o Lab 03 e quantifique lacunas.
3. Execute a query de hunting e selecione uma relação para revisão.
4. Retorne aos eventos originais para recuperar conta, ProcessGuid, horário e linha de comando. Procure tarefa agendada, instalação ou mudança que explique o comportamento.
5. Registre hipótese confirmada, refutada ou inconclusiva; raridade sozinha não confirma nada.
6. Proponha melhoria de coleta ou detecção somente se houver dados suficientes. Não bloqueie processos a partir deste ranking.

## Logs gerados

WindowsEvent / Microsoft-Windows-Sysmon / EventID 1. Reter contexto original em armazenamento privado.

## Evidências

TODO: adicionar evidência real do laboratório

Guardar XML/EVTX bruto fora do Git; publicar somente campos e capturas anonimizados, com horário e contexto.

## Investigação

Confirme provedor, janela UTC e entidade. Separe ator de alvo e evento de interpretação. Procure explicação legítima; documente campos ausentes, perda de coleta e o que os dados não provam.

## Query

[Query e explicação](../../queries/kql/06-hunt-powershell.md) · [Arquivo KQL](../../queries/kql/06-hunt-powershell.kql). Inclui intenção, operadores, falsos positivos e melhorias.

## Regra de detecção

Hunt exploratório, sem alerta automático. Uma futura regra exige padrão estável, falsos positivos conhecidos e testes no ambiente.

## MITRE ATT&CK

[T1059.001 — PowerShell](https://attack.mitre.org/techniques/T1059/001/) descreve o comportamento pesquisado. A técnica pode estar presente em uso legítimo; não inferir intenção.

## Resultado esperado

Ranking reproduzível e uma hipótese revisada com contexto. Se não houver eventos ou baseline, concluir insuficiência de dados, não ausência de ameaça.

## Resultado obtido

Não executado. TODO: adicionar evidência real do laboratório

## O que aprendi

Preencher após executar: qual hipótese mudou, qual campo foi decisivo e qual limitação permaneceu. TODO: adicionar evidência real do laboratório

## Possíveis melhorias

Validar parser, normalização de contas, deduplicação, atraso e baseline. Expandir somente após confirmar o cenário mínimo.

## Próximos passos

Concluir limpeza descrita na execução, registrar resultado real e revisar a detecção com o [template](../../08-Detection-Engineering/TEMPLATE-DETECCAO.md).
