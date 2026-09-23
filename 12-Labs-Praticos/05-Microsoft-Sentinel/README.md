# Lab 05 — Coleta e investigação no Sentinel

[← Índice dos labs](../README.md) · [← Voltar para página principal](../../README.md)

**Status: roteiro introdutório; execução e evidências pendentes.**

## Objetivo

Montar e verificar o caminho entre evento Windows e consulta no workspace.

## Cenário

Um host de laboratório com coleta Windows Security Events via AMA para SecurityEvent; Sysmon é uma coleta adicional, validada separadamente.

## Arquitetura

VM Windows em rede de laboratório → canal de eventos local → agente/regra de coleta, quando configurados → Log Analytics/Sentinel. Os Labs 01–03 podem começar apenas pelo Event Viewer; KQL exige fonte correspondente. Nenhum ambiente foi provisionado por este repositório.

## Pré-requisitos

Assinatura e permissões adequadas, orçamento definido, região e retenção revisadas. Custos de ingestão e serviços associados devem ser conferidos antes de criar recursos. Host fora do Azure pode exigir Azure Arc e seus pré-requisitos.

## Ferramentas utilizadas

Windows, Event Viewer e PowerShell; Sysmon quando aplicável; Microsoft Sentinel/Log Analytics para KQL. Registrar versões reais ao executar.

## Execução

1. Planeje grupo de recursos exclusivo, região, volume e retenção; configure alertas de orçamento, que não impedem gastos automaticamente.
2. Crie ou selecione workspace de laboratório e habilite Sentinel conforme a documentação oficial.
3. No catálogo de conectores, siga Windows Security Events via AMA: associe DCR ao host e inclua os eventos necessários aos labs. Confirme política de auditoria no Windows.
4. Gere um 4625 benigno e verifique SecurityEvent por computador e horário. Não considere só o estado visual do conector.
5. Para Sysmon, siga o [roteiro WEF → coletor → AMA → WindowsEvent](../../06-Microsoft-Sentinel/sysmon-wef.md), com filtro e consulta de conferência. Confirme tabela e propriedades reais; não suponha que o conector Security colete Sysmon.
6. Execute a query de saúde, compare com inventário e documente atraso.
7. Ao terminar, remova associações e recursos criados exclusivamente para o lab após salvar notas; confira custos e recursos remanescentes.

## Logs gerados

SecurityEvent para eventos de segurança no caminho escolhido; WindowsEvent para Sysmon somente após confirmar essa configuração de coleta.

## Evidências

TODO: adicionar evidência real do laboratório

Guardar XML/EVTX bruto fora do Git; publicar somente campos e capturas anonimizados, com horário e contexto.

## Investigação

Confirme provedor, janela UTC e entidade. Separe ator de alvo e evento de interpretação. Procure explicação legítima; documente campos ausentes, perda de coleta e o que os dados não provam.

## Query

[Query e explicação](../../queries/kql/05-saude-coleta.md) · [Arquivo KQL](../../queries/kql/05-saude-coleta.kql). Inclui intenção, operadores, falsos positivos e melhorias.

## Regra de detecção

Monitorar última chegada com inventário esperado. A query isolada não identifica host sem qualquer evento nas últimas 24h. Não habilitar contenção automática.

## MITRE ATT&CK

Coleta é uma capacidade de visibilidade, não uma técnica adversária; não atribuir técnica ao simples provisionamento do SIEM.

## Resultado esperado

Um evento conhecido encontrado ponta a ponta, com tabela e campos confirmados. Teste negativo: host esperado ausente deve ser identificado pela comparação com inventário.

## Resultado obtido

Não executado. TODO: adicionar evidência real do laboratório

## O que aprendi

Preencher após executar: qual hipótese mudou, qual campo foi decisivo e qual limitação permaneceu. TODO: adicionar evidência real do laboratório

## Possíveis melhorias

Validar parser, normalização de contas, deduplicação, atraso e baseline. Expandir somente após confirmar o cenário mínimo.

## Próximos passos

Concluir limpeza descrita na execução, registrar resultado real e revisar a detecção com o [template](../../08-Detection-Engineering/TEMPLATE-DETECCAO.md).
