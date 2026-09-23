# Lab 04 — Falhas seguidas de login com sucesso

[← Índice dos labs](../README.md) · [← Voltar para página principal](../../README.md)

**Status: roteiro introdutório; execução e evidências pendentes.**

## Objetivo

Correlacionar falhas anteriores a um sucesso sem confundir ordem, conta ou origem.

## Cenário

Sequência controlada com conta de teste; começar pela matriz sintética. Não executar brute force contra serviços reais.

## Arquitetura

VM Windows em rede de laboratório → canal de eventos local → agente/regra de coleta, quando configurados → Log Analytics/Sentinel. Os Labs 01–03 podem começar apenas pelo Event Viewer; KQL exige fonte correspondente. Nenhum ambiente foi provisionado por este repositório.

## Pré-requisitos

Audit Logon Success e Failure; mesmos campos preenchidos em 4624 e 4625. Política de bloqueio conhecida. Se cinco falhas excederem o limite permitido, manter teste sintético ou reduzir o limiar apenas na cópia de teste, documentando a alteração.

## Ferramentas utilizadas

Windows, Event Viewer e PowerShell; Sysmon quando aplicável; Microsoft Sentinel/Log Analytics para KQL. Registrar versões reais ao executar.

## Execução

1. Revise a query e sua janela móvel de 10 minutos.
2. Execute o [teste sintético completo](../../queries/tests/README.md), que fornece dados e resultados esperados para dez cenários, sem depender de SecurityEvent real.
3. Se o ambiente permitir, reproduza manualmente a sequência em rede interna e mesma origem, sem desativar proteções.
4. Confira conta, IP, host e LogonType em ambos os eventos; logon interativo local pode não ter IP e ficará fora da query.
5. Execute a consulta e investigue resultados. Encerre sessões e remova somente recursos temporários criados pelo exercício.

## Logs gerados

Security / 4625 e 4624, com TimeGenerated, TargetAccount, Computer, IpAddress e LogonType coerentes.

## Evidências

TODO: adicionar evidência real do laboratório

Guardar XML/EVTX bruto fora do Git; publicar somente campos e capturas anonimizados, com horário e contexto.

## Investigação

Confirme provedor, janela UTC e entidade. Separe ator de alvo e evento de interpretação. Procure explicação legítima; documente campos ausentes, perda de coleta e o que os dados não provam.

## Query

[Query e explicação](../../queries/kql/04-falhas-seguidas-sucesso.md) · [Arquivo KQL](../../queries/kql/04-falhas-seguidas-sucesso.kql). Inclui intenção, operadores, falsos positivos e melhorias.

## Regra de detecção

Candidata experimental: cinco falhas em dez minutos antes de um sucesso; frequência sugerida de cinco minutos apenas para avaliação. A query cobre uma hora de sucessos e pode gerar repetição: ajustar agrupamento e deduplicação antes de habilitar. Severidade média provisória, dependente de contexto.

## MITRE ATT&CK

[T1110.001 — Password Guessing](https://attack.mitre.org/techniques/T1110/001/) como hipótese. Sucesso não comprova abuso de conta válida nem comprometimento.

## Resultado esperado

Cinco falhas anteriores na mesma chave produzem um resultado; quatro, posteriores, antigas ou com chave diferente não. Exatamente dez minutos antes é incluído; mesmo timestamp do sucesso é excluído.

## Resultado obtido

Não executado. TODO: adicionar evidência real do laboratório

## O que aprendi

Preencher após executar: qual hipótese mudou, qual campo foi decisivo e qual limitação permaneceu. TODO: adicionar evidência real do laboratório

## Possíveis melhorias

Validar parser, normalização de contas, deduplicação, atraso e baseline. Expandir somente após confirmar o cenário mínimo.

## Próximos passos

Concluir limpeza descrita na execução, registrar resultado real e revisar a detecção com o [template](../../08-Detection-Engineering/TEMPLATE-DETECCAO.md).
