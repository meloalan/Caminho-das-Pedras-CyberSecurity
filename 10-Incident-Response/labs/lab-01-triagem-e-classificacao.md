# Lab 01: triagem e classificação

[← Labs](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md) · [Lab 02 →](lab-02-timeline.md)

**Objetivo:** separar fato, inferência e desconhecido em um alerta de origem atípica. **Cenário:** `CASE-LAB-101` alerta para `LAB-EXEC`. **Arquitetura:** dataset JSONL local, sem serviços externos. **Pré-requisitos:** ler [detecção e análise](../detection-and-analysis.md) e [classificação](../classification-and-severity.md). **Ferramentas utilizadas:** editor de texto ou planilha local.

## Execução

1. Abra [incident-events.jsonl](data/incident-events.jsonl) e localize `EVT-001`, `EVT-002` e `EVT-004`.
2. Para cada registro, anote event time, ingestion time, fonte e o que o dado realmente demonstra.
3. Escreva duas explicações plausíveis, uma legítima e uma que exija resposta.
4. Liste três desconhecidos e a fonte ou pessoa que pode validá-los.
5. Indique se os critérios fictícios da organização exigem abrir incidente, escalar ou continuar triagem. Justifique sem tratar o alerta como prova.

**Logs gerados:** nenhum, somente leitura do dataset. **Evidências:** tabela de fatos, hipóteses, desconhecidos e decisão. **Investigação:** verifique identidade, dispositivo, MFA e aplicação sem presumir relação causal.

### Query orientadora

```text
Filtrar incident-events.jsonl onde entity = LAB-EXEC
e event_time entre 2026-09-29T01:00:00Z e 2026-09-29T02:00:00Z
ordenar por event_time, mantendo ingestion_time
```

É pseudoconsulta independente de plataforma. **Regra de detecção:** nenhuma regra nova é necessária. **MITRE ATT&CK:** não atribua técnica com base apenas em origem inesperada. **Resultado esperado:** uma decisão provisória proporcional com limitações. **Resultado obtido:** preencha com o que você observou no dataset.

**O que aprendi:** qual fonte mudaria sua decisão? **Segurança:** dados inteiramente sintéticos; nenhuma ação em produção. **Desafio:** escreva um SITREP de três frases. **Referências:** páginas de [detecção](../detection-and-analysis.md) e [severidade](../classification-and-severity.md).

---

[← Labs](README.md) · [↑ Módulo 10](../README.md) · [Página principal](../../README.md) · [Lab 02 →](lab-02-timeline.md)
