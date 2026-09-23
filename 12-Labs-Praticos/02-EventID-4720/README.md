# Lab 02 — Criação de usuário (4720)

[← Índice dos labs](../README.md) · [← Voltar para página principal](../../README.md)

**Status: roteiro introdutório; execução e evidências pendentes.**

## Objetivo

Identificar criação de conta e distinguir ator, alvo e escopo local.

## Cenário

Criação autorizada de conta local descartável em VM que não é controlador de domínio.

## Arquitetura

VM Windows em rede de laboratório → canal de eventos local → agente/regra de coleta, quando configurados → Log Analytics/Sentinel. Os Labs 01–03 podem começar apenas pelo Event Viewer; KQL exige fonte correspondente. Nenhum ambiente foi provisionado por este repositório.

## Pré-requisitos

Permissão administrativa na VM; Account Management → Audit User Account Management → Success habilitada. Escolher um nome exclusivo de laboratório e nunca reutilizar uma conta existente.

## Ferramentas utilizadas

Windows, Event Viewer e PowerShell; Sysmon quando aplicável; Microsoft Sentinel/Log Analytics para KQL. Registrar versões reais ao executar.

## Execução

1. Faça snapshot e registre a política de auditoria efetiva.
2. Em PowerShell elevado, use `$labPassword = Read-Host "Senha temporária" -AsSecureString` e depois `New-LocalUser -Name "lab-estudo-4720" -Password $labPassword -Description "Conta temporária do lab"`. Não adicione a Administradores.
3. Filtre Security por 4720 e examine SubjectUserName, TargetUserName e TargetSid.
4. Confirme que a conta foi criada no computador local, não no domínio. Compare com a query.
5. Remova apenas a conta criada neste exercício com `Remove-LocalUser -Name "lab-estudo-4720"` após conferir seu nome e origem.

## Logs gerados

Security / Microsoft-Windows-Security-Auditing / 4720. A remoção pode gerar 4726; registre separadamente.

## Evidências

TODO: adicionar evidência real do laboratório

Guardar XML/EVTX bruto fora do Git; publicar somente campos e capturas anonimizados, com horário e contexto.

## Investigação

Confirme provedor, janela UTC e entidade. Separe ator de alvo e evento de interpretação. Procure explicação legítima; documente campos ausentes, perda de coleta e o que os dados não provam.

## Query

[Query e explicação](../../queries/kql/02-conta-criada.md) · [Arquivo KQL](../../queries/kql/02-conta-criada.kql). Inclui intenção, operadores, falsos positivos e melhorias.

## Regra de detecção

Baseline de 4720 com severidade baixa para estudo. Provisionamento aprovado é comum. Validar conta criada, ator e janela; consultar também a regra Sigma experimental.

## MITRE ATT&CK

[T1136 — Create Account](https://attack.mitre.org/techniques/T1136/) → [T1136.001 — Local Account](https://attack.mitre.org/techniques/T1136/001/). O mapeamento vale porque este roteiro cria conta local. A atividade é benigna e autorizada.

## Resultado esperado

Evento 4720 correspondente à nova conta local, ator administrativo identificável e remoção confirmada ao final. Conta preexistente não deve ser alterada.

## Resultado obtido

Não executado. TODO: adicionar evidência real do laboratório

## O que aprendi

Preencher após executar: qual hipótese mudou, qual campo foi decisivo e qual limitação permaneceu. TODO: adicionar evidência real do laboratório

## Possíveis melhorias

Validar parser, normalização de contas, deduplicação, atraso e baseline. Expandir somente após confirmar o cenário mínimo.

## Próximos passos

Concluir limpeza descrita na execução, registrar resultado real e revisar a detecção com o [template](../../08-Detection-Engineering/TEMPLATE-DETECCAO.md).
