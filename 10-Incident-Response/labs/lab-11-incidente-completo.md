# Lab 11: incidente integrado

[← Lab 10](lab-10-lessons-learned.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Módulo 11: MITRE ATT&CK →](../../11-MITRE-ATTACK/README.md)

**Objetivo:** produzir um pacote integrado de resposta com fatos, escopo, decisão, contenção, recuperação e melhoria. **Cenário:** `CASE-LAB-101`, identidade privilegiada e endpoint potencialmente relacionado. **Arquitetura:** somente dataset JSONL local e tabletop. **Pré-requisitos:** concluir labs 01 a 10. **Ferramentas:** templates do módulo.

## Execução

1. Faça triagem e registre critérios de classificação fictícios.
2. Construa timeline mantendo event time, ingestion time e hora da detecção.
3. Mapeie identidade, sessões, aplicação e endpoint; marque limites de cobertura.
4. Escreva decisão de contenção comparando ação ampla, parcial e observação temporária.
5. Produza SITREP e handoff acionável.
6. Planeje erradicação da causa ainda hipotética e indique quais fatos faltam para confirmar.
7. Avalie EVT-013 e EVT-014 como registros de exercício, não prova de backup real.
8. Defina critérios de retorno, monitoramento e encerramento.
9. Faça tabletop de comunicação e escalonamento. Gere lições com donos e teste.

**Logs gerados:** nenhum real. **Evidências:** registros construídos pelo estudante a partir de dados fictícios. **Investigação:** cada conclusão deve ter fonte. **Query:** operações conceituais por entidade, sessão e tempo. **Regra de detecção:** não é necessário construir regra. **MITRE ATT&CK:** mapeie somente se comportamento sustentar técnica; documente confiança e fonte, caso contrário deixe sem mapeamento.

## Entrega mínima do exercício

1. Resumo e classificação provisória.
2. Timeline de ao menos cinco linhas com fontes e fuso.
3. Mapa de escopo e lacunas.
4. Decision log com alternativas, autoridade, reversão e reavaliação.
5. Registro de evidências e limitações.
6. SITREP e handoff.
7. Plano de erradicação e recuperação com validação.
8. Checklist de encerramento e risco residual.
9. Lessons learned com três ações testáveis.

**Resultado esperado:** evidência, inferência e desconhecido separados; decisão proporcional e revisável; nenhum alerta automaticamente considerado incidente. **Resultado obtido:** registre análise real do dataset. **O que aprendi:** que informação mais alteraria a decisão? **Segurança:** nenhuma ação ou dado de produção. **Desafio:** apresente o caso em três minutos a liderança fictícia. **Referências:** [framework](../incident-response-framework.md) e [templates](../README.md).

---

[← Lab 10](lab-10-lessons-learned.md) · [↑ Labs](README.md) · [Página principal](../../README.md) · [Módulo 11: MITRE ATT&CK →](../../11-MITRE-ATTACK/README.md)
