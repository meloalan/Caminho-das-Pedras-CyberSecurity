# Lab 04: decisões de contenção

[← Lab 03](lab-03-scoping.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 05 →](lab-05-identity-compromise.md)

**Objetivo:** comparar contenção ampla, parcial e observação temporária com prazo. **Cenário:** `LAB-EXEC` tem duas sessões simuladas e serviço dependente. **Arquitetura:** tabletop com dataset local. **Pré-requisitos:** [containment](../containment.md) e [decision log](../decision-log.md). **Ferramentas:** templates do módulo.

## Execução

Para cada opção abaixo, avalie benefício, risco de esperar, impacto operacional, evidência que pode perder, reversibilidade, autoridade e validação:

1. Suspender toda a identidade.
2. Revogar apenas sessão observada e validar a segunda em paralelo.
3. Observar por janela curta definida pelo facilitador enquanto se valida titular e sessão.

Considere EVT-001 a EVT-012, mas diferencie decisão simulada de ação real. Registre opção, aprovador, executor, prazo/gatilho e estado que mudaria a escolha. Não há resposta única: fatos e política local controlam a decisão.

**Logs gerados:** nenhum; exercício escrito. **Evidências:** tabela comparativa e [log de decisão](../TEMPLATE-DECISION-LOG.md). **Query:** filtro por `session_ref` e `entity`, preservando as fontes. **Regra de detecção:** não automatizar ação a partir do alerta. **MITRE ATT&CK:** não aplicável sem evidência comportamental suficiente.

**Resultado esperado:** justificativa explícita e próxima reavaliação. **Resultado obtido:** registre seu argumento. **O que aprendi:** que fato faria agir imediatamente? **Segurança:** não execute alterações. **Desafio:** altere criticidade do serviço e reavalie. **Referência:** [contenção](../containment.md).

---

[← Lab 03](lab-03-scoping.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 05 →](lab-05-identity-compromise.md)
