# Lab 01 — Falhas de autenticação (4625)

[← Índice dos labs](../README.md) · [← Voltar para página principal](../../README.md)

**Status: roteiro introdutório; execução e evidências pendentes.**

## Objetivo

Investigar uma falha de autenticação Windows sem assumir que ela é maliciosa.

## Cenário

Uma conta local de teste em VM Windows independente, com uma tentativa manual de senha incorreta.

## Arquitetura

VM Windows em rede de laboratório → canal de eventos local → agente/regra de coleta, quando configurados → Log Analytics/Sentinel. Os Labs 01–03 podem começar apenas pelo Event Viewer; KQL exige fonte correspondente. Nenhum ambiente foi provisionado por este repositório.

## Pré-requisitos

Auditoria avançada: Logon/Logoff → Audit Logon → Failure habilitada e confirmada na política efetiva. Conhecer a política de bloqueio antes do teste; uma única tentativa basta. Para KQL, executar antes o Lab 05.

## Ferramentas utilizadas

Windows, Event Viewer e PowerShell; Sysmon quando aplicável; Microsoft Sentinel/Log Analytics para KQL. Registrar versões reais ao executar.

## Execução

1. Registre snapshot e horário UTC. Confirme que a conta de teste não é usada por serviços.
2. Faça uma tentativa manual com senha incorreta, sem automação.
3. Abra Security e filtre 4625. Compare TargetUserName, TargetDomainName, LogonType, Status e SubStatus no XML.
4. Quando houver coleta, execute a query correspondente no workspace e compare o evento.
5. Encerre a sessão de teste e preserve somente notas anonimizadas.

## Logs gerados

Security, provedor Microsoft-Windows-Security-Auditing, EventID 4625; IP pode estar vazio em logon local.

## Evidências

TODO: adicionar evidência real do laboratório

Guardar XML/EVTX bruto fora do Git; publicar somente campos e capturas anonimizados, com horário e contexto.

## Investigação

Confirme provedor, janela UTC e entidade. Separe ator de alvo e evento de interpretação. Procure explicação legítima; documente campos ausentes, perda de coleta e o que os dados não provam.

## Query

[Query e explicação](../../queries/kql/01-falhas-autenticacao.md) · [Arquivo KQL](../../queries/kql/01-falhas-autenticacao.kql). Inclui intenção, operadores, falsos positivos e melhorias.

## Regra de detecção

Triagem de cada 4625 em modo de estudo; não gerar alerta de alta severidade para toda falha. Avaliar baseline e tipo de logon antes de adotar limiar.

## MITRE ATT&CK

Uma falha isolada não demonstra uma técnica. Repetição de tentativas de senha pode sustentar [T1110.001](https://attack.mitre.org/techniques/T1110/001/) conforme o contexto.

## Resultado esperado

Encontrar o 4625 correspondente à tentativa, com conta e horário coerentes. Controle negativo: a query de 4625 não deve selecionar um 4624.

## Resultado obtido

Não executado. TODO: adicionar evidência real do laboratório

## O que aprendi

Preencher após executar: qual hipótese mudou, qual campo foi decisivo e qual limitação permaneceu. TODO: adicionar evidência real do laboratório

## Possíveis melhorias

Validar parser, normalização de contas, deduplicação, atraso e baseline. Expandir somente após confirmar o cenário mínimo.

## Próximos passos

Concluir limpeza descrita na execução, registrar resultado real e revisar a detecção com o [template](../../08-Detection-Engineering/TEMPLATE-DETECCAO.md).
