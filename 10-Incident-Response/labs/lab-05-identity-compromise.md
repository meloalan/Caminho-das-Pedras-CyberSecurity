# Lab 05: suspeita de comprometimento de identidade

[← Lab 04](lab-04-containment-decisions.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 06 →](lab-06-endpoint-incident.md)

**Objetivo:** investigar conta executiva, avaliar privilégio, sessões e containment, documentar decisão e passar handoff. **Cenário:** `LAB-EXEC`, origem inesperada e eventos com ingestão atrasada. **Arquitetura:** dataset JSONL. **Pré-requisitos:** playbook de [identidade](../playbooks/identity-compromise.md). **Ferramentas:** editor e templates.

## Execução

1. Analise EVT-001 a EVT-007. Registre o que autenticação aceita e MFA aceito demonstram e o que não demonstram.
2. Monte timeline, hipóteses legítimas e adversas, confiança, privilégios e lacunas.
3. Defina como validar titular por canal independente e revisar sessões e aplicações.
4. Avalie suspensão total, restrição parcial e validação paralela; registre autoridade, impacto e reversibilidade.
5. Escreva SITREP técnico, decisão e handoff com próximo passo e gatilho de escalonamento.

**Logs gerados:** nenhum. **Evidências:** timeline, escopo e registros de decisão. **Query:** filtrar `entity=LAB-EXEC` e agrupar por `session_ref`, sem descartar horas de ingestão. **Regra:** nenhuma nova detecção. **ATT&CK:** não concluir técnica apenas por origem geográfica.

**Resultado esperado:** decisão calibrada, afirmações apoiadas por fontes e handoff acionável. **Resultado obtido:** complete os templates. **O que aprendi:** qual dado faltante mais muda risco? **Segurança:** nenhum acesso real; o dataset é fictício. **Desafio:** conduza handoff para colega que não leu o caso. **Referência:** [template de handoff](../TEMPLATE-HANDOFF.md).

---

[← Lab 04](lab-04-containment-decisions.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 06 →](lab-06-endpoint-incident.md)
