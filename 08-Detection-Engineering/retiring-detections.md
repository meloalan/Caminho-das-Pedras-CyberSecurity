# Aposentar sem perder rastreabilidade

<!-- markdownlint-configure-file {"MD033": {"allowed_elements": ["details", "summary"]}} -->

[← Tópico anterior](versioning.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](anti-patterns.md)

## Quando considerar aposentadoria

Tecnologia desativada, fonte removida, substituição por outra capacidade, comportamento fora do risco atual ou migração de plataforma podem justificar aposentadoria. Muito alerta, isoladamente, pede investigação antes de desligamento.

## Registro de decisão

| Campo | Exemplo fictício |
| --- | --- |
| Artefato | DET-LAB-LEGACY-001 |
| Motivo | Serviço de laboratório desativado |
| Evidência | Inventário e mudança aprovados |
| Data efetiva | A definir no plano de mudança |
| Substituição | Nova fonte/artefato, ou nenhuma com risco aceito |
| Impacto | Quais comportamentos deixam de ser observados |
| Responsável e aprovação | Owner e responsável pelo risco |
| Reversão | Condições e procedimento de reativação |

## Processo de saída

1. Conferir dependências: dashboards, correlações compostas, runbooks e alertas de saúde.
2. Comparar a capacidade substituta com os mesmos casos de teste e população.
3. Planejar período de coexistência ou transição conforme o risco.
4. Desabilitar de forma controlada, registrar evidência e atualizar inventário.
5. Arquivar versão e motivo; atualizar links e matriz de cobertura.

Não delete silenciosamente o histórico. A auditoria precisa entender se uma regra ausente foi substituída ou se a capacidade deixou de existir. Uma fonte removida pode exigir reabrir o risco, não marcar o caso como concluído.

## Exercício de revisão

A organização migrou de SIEM e a busca antiga não executa mais. O novo produto possui uma regra de nome parecido. Antes de aposentar, compare fontes, campos, janela, entidades, casos positivos e negativos, agrupamento e runbook. Nome parecido não é prova de substituição funcional.

## Checkpoint

**Uma regra substituta com a mesma tag ATT&CK basta para aposentar a antiga?**

<details>
<summary>Ver resposta</summary>

Não. É necessário comparar comportamento, população, telemetria, testes e impacto da transição.

</details>

[← Tópico anterior](versioning.md) · [↑ Índice do módulo](README.md) · [Página principal](../README.md) · [Próximo tópico →](anti-patterns.md)
