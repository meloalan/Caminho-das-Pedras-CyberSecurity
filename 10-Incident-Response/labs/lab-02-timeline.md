# Lab 02: timeline e normalização de horários

[← Lab 01](lab-01-triagem-e-classificacao.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 03 →](lab-03-scoping.md)

**Objetivo:** construir timeline sem confundir ocorrência, ingestão e detecção. **Cenário:** eventos sintéticos do caso `CASE-LAB-101`. **Arquitetura:** JSONL local. **Pré-requisitos:** [página de timeline](../incident-timeline.md). **Ferramentas:** planilha ou editor.

## Execução

1. Extraia EVT-001 a EVT-007 e mantenha ambas as colunas temporais.
2. Ordene por event time e compare com ordenação por ingestion time.
3. Acrescente o alerta, contato e diferença entre observação técnica e nota de analista.
4. Normalize somente horários com fuso conhecido. Marque incerteza onde não se sabe a zona.
5. Registre a ordem que mudaria se usasse apenas ingestion time.

**Logs gerados:** nenhum. **Evidências:** timeline com fonte, entidade, confiança e limitações. **Investigação:** EVT-003 e EVT-006 têm atraso. **Query:** filtro conceitual por `event_time`, preservando `ingestion_time`. **Regra de detecção:** não aplicável. **MITRE ATT&CK:** não inferir técnica por ordem temporal.

**Resultado esperado:** detecção posterior a parte dos eventos, sem provar causalidade. **Resultado obtido:** anote sua própria tabela. **O que aprendi:** que ordenação é mais útil e por quê? **Segurança:** dataset fictício. **Desafio:** acrescente horário de notificação e decisão simulada. **Referência:** [timeline](../incident-timeline.md).

---

[← Lab 01](lab-01-triagem-e-classificacao.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Lab 03 →](lab-03-scoping.md)
