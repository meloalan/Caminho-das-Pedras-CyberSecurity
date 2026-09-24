# Lab 07: Tuning com regressão

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](lab-06-detection-rule.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-investigation.md)

> Pergunta: o ajuste remove ruído ou esconde cobertura?

## Objetivo e pré-requisitos

Melhorar uma regra de autenticação fictícia sem generalizar exceções. Leia [tuning](../tuning.md) e use a especificação do Lab 06 como modelo de documentação, escolhendo um caso de uso de 4625 separado.

## Execução

1. Descreva o problema de “qualquer 4625 gera High”.
2. Proponha uma única mudança, como chave de conta+domínio e janela.
3. Teste falhas relevantes, benignas, homônimas e campos vazios.
4. Proponha uma exceção apenas para svc-lab em host e contexto autorizados.
5. Teste a mesma conta em outro host e fora do contexto.
6. Compare a versão antes/depois e declare casos potencialmente perdidos.
7. Defina owner, validade da exceção, revisão e rollback.

## Camada alterada por plataforma

Wazuh: rule/condições ou limiar de notificação, sem confundir com archives. Splunk: SPL versus throttle/schedule. QRadar: CRE/building block versus reference set/resposta. Sentinel: KQL versus supressão/agrupamento. Registre exatamente qual camada explica a diferença.

## Resultado esperado

Uma mudança justificada que tem teste de regressão. Reduzir candidatos não é suficiente. O dataset pequeno serve para demonstrar um contraexemplo, não para estimar taxa real de falso positivo.

## Entrega

Tabela versão × mudança × resultado × ganho × perda, mais uma hipótese que exigiria detecção complementar. Critério de conclusão: conseguir defender e também criticar o próprio ajuste.

## Resultado obtido

Preencha após sua execução: percurso, versão quando aplicável, evidência, divergências e limitações. Não marque configuração de produto como validada com base apenas na análise offline.

## Checkpoint

**Qual evidência sustenta sua entrega?**

<details>
<summary>Ver resposta</summary>

Registre fonte, janela, consulta ou cálculo, resultado e limite. Uma descrição do que deveria ocorrer não substitui resultado obtido.

</details>

[← Tópico anterior](lab-06-detection-rule.md) · [↑ Índice do módulo](../README.md) · [Página principal](../../README.md) · [Próximo tópico →](lab-08-investigation.md)
