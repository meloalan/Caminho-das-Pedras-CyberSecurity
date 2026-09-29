# Lab 03: escopo orientado por evidência

[← Lab 02](lab-02-timeline.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 04 →](lab-04-containment-decisions.md)

**Objetivo:** expandir a partir de uma conta sem assumir que toda correlação representa comprometimento. **Cenário:** eventos IdP, aplicação e endpoint sintéticos. **Arquitetura:** JSONL. **Pré-requisitos:** [scoping](../scoping.md). **Ferramentas:** editor ou quadro de grafo.

## Execução

1. Parta de `LAB-EXEC` e relacione somente entidades com suporte no dataset.
2. Examine sessão, aplicação, dispositivo e usuário.
3. Use EVT-010 para discutir cobertura parcial e EVT-008 para confiança baixa.
4. Classifique cada nó confirmado, possível, descartado ou desconhecido e justifique.
5. Proponha duas consultas adicionais por pergunta operacional, não por curiosidade.

**Logs gerados:** nenhum. **Evidências:** grafo com fonte e relação. **Investigação:** não declare endpoint comprometido por um alerta genérico. **Query:** busca conceptual por `entity`, `session_ref`, `application` e janela temporal. **Regra de detecção:** não criar regra para este exercício. **MITRE ATT&CK:** sem atribuição técnica suficiente.

**Resultado esperado:** escopo parcial, limitações explícitas e próximos pivôs. **Resultado obtido:** preencha o grafo. **O que aprendi:** quais ausências são inconclusivas? **Segurança:** dados sintéticos apenas. **Desafio:** mostre como uma fonte ausente altera a confiança. **Referência:** [scoping](../scoping.md).

---

[← Lab 02](lab-02-timeline.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 04 →](lab-04-containment-decisions.md)
