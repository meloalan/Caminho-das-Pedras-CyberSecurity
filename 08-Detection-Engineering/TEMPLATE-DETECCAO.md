# Template de regra de detecção

[← Índice](README.md) · [Página principal](../README.md)

## Identificação

- Nome, ID estável, versão, autor e responsável: preencher.
- Status: rascunho → experimental → validada no lab → candidata à produção.
- Data e ambiente de validação: ainda não executada.

## Caso de uso

Descreva risco, comportamento observável, ativo protegido e decisão que o analista poderá tomar.

## Fonte e telemetria

Documente provedor, canal, tabela, campos obrigatórios, normalização, retenção, política de auditoria e teste de saúde da coleta.

## Lógica

Vincule a query versionada. Declare janela, frequência, limiar, chaves de correlação, ordenação temporal, tratamento de nulos, atrasos e duplicatas.

## Alerta e severidade

Justifique impacto e confiança separadamente. Defina entidades, agrupamento, proprietário, playbook e critérios de escalonamento.

## False positives e tuning

Liste cenários legítimos. Toda exceção deve ter escopo, dono, motivo, prazo e teste contra perda de cobertura.

## MITRE ATT&CK

Informe técnica/subtécnica, URL oficial, evidência que sustenta o mapeamento e o comportamento que permanece invisível.

## Validação e testes

| Caso | Entrada | Resultado esperado | Resultado obtido |
| --- | --- | --- | --- |
| Positivo | Comportamento definido | Alerta contextualizado | Pendente |
| Negativo | Atividade fora da lógica | Sem alerta | Pendente |
| Limite | Limiar exato e janela temporal | Conforme especificação | Pendente |
| Qualidade | Campo vazio, duplicata e atraso | Limitação registrada | Pendente |

TODO: adicionar evidência real do laboratório

## Operação e manutenção

Registre custo/volume de consulta, alertas por período, classificação após triagem, revisão de exceções e procedimento de desativação. Não promova a produção sem testes no ambiente alvo.
